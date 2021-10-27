/** 
 * JS for add manual nms data (DEVICE)
 **/

$(document).ready(function() {
    // ==== Global Variables ====
    MANUAL_NMS_DATA = {};
    JWT_ACCESS = Cookies.get('aid-token-access');
    JWT_REFRESH = Cookies.get('aid-token-refresh');
    MANDATORY_FIELDS = {
        'DEVICE':   ['site_id', 'subdomain', 'ems_id', 'device_id'],
        'CELL':     ['site', 'subdomain', 'band', 'ems_id', 'cell_name', 'parent_id'],
        'TRX':      ['ems_id', 'trx_name', 'parent_id', 'homing_bts', 'homing_id']
    };
    NMS_DATA_FORMS = {
        'DEVICE': $("#id-add-device-form"),
        'CELL': $("#id-add-cell-form"),
        'TRX': $("#id-add-trx-form")
    };

    function Device(){
        this.id = null;
        this.dn = null;
        this.device_id = null;
        this.ems_device_id = null;
        this.device_alias = null;
        this.device_ip = null;
        this.ems_id = null;
        this.vendor_id = null;
        this.ne_type = null;
        this.model = null;
        this.hardware_description = null;
        this.functional_description = null;
        this.parent_device_id = null;
        this.parentdn = null;
        this.site_id = null;
        this.device_state = null;
        this.software_version = null;
        this.integration_date = null;
        this.end_of_support = null;
        this.tsa_scope = null;
        this.product_id = null;
        this.serial_number = null;
        this.freq_tx_rx_field = null;
        this.hardware_capacity = null;
        this.domain = null;
        this.ne_owner = null;
        this.tx_clusterimg = null;
        this.tx_type = null;
        this.natspcode = null;
        this.admin_state = null;
        this.subdomain = null;
        this.function = null;
        this.iubce_dl_lic = null;
        this.iubce_ul_lic = null;
        this.s1cu_lic = null;
        this.record_status = null;
    };

    function Cell(){
        this.id = null;
        this.domain = null;
        this.ems_cell_id = null;
        this.ems_id = null;
        this.cell_name = null;
        this.dn = null;
        this.site = null;
        this.parent_id = null;
        this.parent_dn = null;
        this.tech = null;
        this.band = null;
        this.admin_state = null;
        this.alias = null;
        this.lac_tac = null;
        this.sac_ci_eutra = null;
        this.rnc_cid = null;
        this.phy_cid = null;
        this.lcr_cid = null;
        this.mcc = null;
        this.mnc = null;
        this.nodeid = null;
        this.sector_id = null;
        this.carrier = null;
        this.ne_type = null;
        this.subdomain = null;
        this.function = null;
        this.sdcch_cap = null;
        this.tch_cap = null;
        this.homing_id = null;
        this.dlear_fcn = null;
        this.ulear_dcn = null;
        this.dlc_hbw = null;
        this.ulc_hbw = null;
        this.rac = null;
        this. ncc = null;
        this.bcc = null;
        this.nnode_id = null;
        this.nbscid = null;
        this.psc = null;
        this.bccgno = null;
        this.record_status = null;
    }

    function Trx(){
        this.id = null;
        this.ems_trx_id = null;
        this.ems_id = null;
        this.trx_name = null;
        this.dn = null;
        this.site_id = null;
        this.parent_id = null;
        this.parent_dn = null;
        this.admin_state = null;
        this.e1_assignment = null;
        this.homing_bts = null;
        this.homing_id = null;
        this.trxfreq = null;
        this.record_status = null;
    }

    // ==== Function ====
    function get_site_tech_band(){
        selectSiteid = $('#id_siteid').val() ? $('#id_siteid').find(':selected').text() : null;
        selectTech = $('#id_tech').val() ? $('#id_tech').find(':selected').text() : null;
        selectBand = $('#id_band').val() ? $('#id_band').find(':selected').text() : null;
        
        return {'site': selectSiteid, 'tech': selectTech, 'band': selectBand};
    }

    function form_auto_fill(form, field_val_pair){
        form.find('input').each(function(){
            field = $(this).attr('name');
            if(field_val_pair.hasOwnProperty(field)){
                $(this).val(field_val_pair[field]);
            }
        });
    }

    function validate_form(form, mandatory_field_list){
        valid = true;
        form.find('input').each(function(){
            field = $(this).attr('name');
            $(this).removeClass('is-invalid');
            MANUAL_NMS_DATA[field] = $(this).val();
            if(mandatory_field_list.includes(field) && !$(this).val()){
                valid = false;
                $(this).addClass('is-invalid');
            }
        });

        return valid;
    }

    function clear_form(form){
        form.find('input').each(function(){
            $(this).removeClass('is-invalid');
            $(this).val('');
        });
        MANUAL_NMS_DATA = {};
    }

    function show_alert_message(message, alert_type, alert_container){
        alert_html = `<div class="alert ${alert_type} alert-dismissible fade show" role="alert">
            ${message}
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>`;
        alert_container.html(alert_html);
        $('.alert').alert();
    }

    function instantiateObject(dataObject, Obj){
        let MyObj = new Obj();
        for(let [key, val] of Object.entries(MyObj)){
            if(key in dataObject){
                if(dataObject[key]){
                    MyObj[key] = dataObject[key];
                }
            }
        }

        return MyObj;
    }

    async function post_data_to_server(url, data, jwttoken){
        bearer = 'Bearer ' + jwttoken;
        const response = await fetch(url, {
            method: 'POST',
            cache: 'no-cache',
            headers: {
                'Authorization': bearer,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        return response.json();
    }
    
    // ==== Events ====

    /* open add nms data modals */
    $("i#add-device").click(function(){
        $('#add-device-modal').modal({backdrop: 'static', keyboard: false});
        selected_ne = get_site_tech_band();
        form_auto_fill(NMS_DATA_FORMS['DEVICE'], 
            {'site_id': selected_ne['site'], 'subdomain': selected_ne['tech']}
        );
    });

    $("i#add-cell").click(function(){
        $('#add-cell-modal').modal({backdrop: 'static', keyboard: false});
        selected_ne = get_site_tech_band();
        form_auto_fill(NMS_DATA_FORMS['CELL'], 
            {'site': selected_ne['site'], 'subdomain': selected_ne['tech'], 'band': selected_ne['band']}
        );
    });
    
    $("i#add-trx").click(function(){
        $('#add-trx-modal').modal({backdrop: 'static', keyboard: false});
        selected_ne = get_site_tech_band();
        form_auto_fill(NMS_DATA_FORMS['TRX'], 
            {'site_id': selected_ne['site']}
        );
    });

    /* close add nms data modals */
    $("#cancel-add-device").click(function(e){
        e.preventDefault();
        $('#device-alert-container').html('');
        clear_form(NMS_DATA_FORMS['DEVICE']);
    });

    $("#cancel-add-cell").click(function(e){
        e.preventDefault();
        $('#cell-alert-container').html('');
        clear_form(NMS_DATA_FORMS['CELL']);
    });

    $("#cancel-add-trx").click(function(e){
        e.preventDefault();
        $('#trx-alert-container').html('');
        clear_form(NMS_DATA_FORMS['TRX']);
    });

    /* save nms data events */
    $("#save-add-device").click(function(e){
        e.preventDefault();
        isValid = validate_form(NMS_DATA_FORMS['DEVICE'], MANDATORY_FIELDS['DEVICE']);
        if(isValid){
            var DeviceObj = instantiateObject(MANUAL_NMS_DATA, Device);
            post_data_to_server(`/nmsdata/device/`, DeviceObj, JWT_ACCESS)
                .then(function(data){
                    message = data.hasOwnProperty('message')? data.message : `Successfully added <strong>${data.device_id}</strong> in NMS data!`;
                    alert_type = data.hasOwnProperty('message')? `alert-warning` : `alert-success`;
                    show_alert_message(message, alert_type, $('#device-alert-container'));
                    clear_form(NMS_DATA_FORMS['DEVICE']);
                    console.log(data);
                })
                .catch(function(e){
                    message = `Unexpected error occured in adding <strong>${DeviceObj.device_id}</strong> in NMS data.`;
                    show_alert_message(message, 'alert-danger', $('#device-alert-container'));
                    console.log(e);
                });
        }
    });

    $("#save-add-cell").click(function(e){
        e.preventDefault();
        isValid = validate_form(NMS_DATA_FORMS['CELL'], MANDATORY_FIELDS['CELL']);
        if(isValid){
            var CellObj = instantiateObject(MANUAL_NMS_DATA, Cell);
            post_data_to_server(`/nmsdata/cell/`, CellObj, JWT_ACCESS)
                .then(function(data){
                    message = data.hasOwnProperty('message')? data.message : `Successfully added <strong>${data.cell_name}</strong> in NMS data!`;
                    alert_type = data.hasOwnProperty('message')? `alert-warning` : `alert-success`;
                    show_alert_message(message, alert_type, $('#cell-alert-container'));
                    clear_form(NMS_DATA_FORMS['CELL']);
                    console.log(data);
                })
                .catch(function(e){
                    message = `Unexpected error occured in adding <strong>${CellObj.cell_name}</strong> in NMS data.`;
                    show_alert_message(message, 'alert-danger', $('#cell-alert-container'));
                    console.log(e);
                });
        }
    });

    $("#save-add-trx").click(function(e){
        e.preventDefault();
        isValid = validate_form(NMS_DATA_FORMS['TRX'], MANDATORY_FIELDS['TRX']);
        if(isValid){
            var TrxObj = instantiateObject(MANUAL_NMS_DATA, Trx);
            post_data_to_server(`/nmsdata/trx/`, TrxObj, JWT_ACCESS)
                .then(function(data){
                    message = data.hasOwnProperty('message')? data.message : `Successfully added <strong>${data.trx_name}</strong> in NMS data!`;
                    alert_type = data.hasOwnProperty('message')? `alert-warning` : `alert-success`;
                    show_alert_message(message, alert_type, $('#trx-alert-container'));
                    clear_form(NMS_DATA_FORMS['TRX']);
                    console.log(data);
                })
                .catch(function(e){
                    message = `Unexpected error occured in adding <strong>${TrxObj.trx_name}</strong> in NMS data.`;
                    show_alert_message(message, 'alert-danger', $('#trx-alert-container'));
                    console.log(e);
                });
        }
    });
    
});

