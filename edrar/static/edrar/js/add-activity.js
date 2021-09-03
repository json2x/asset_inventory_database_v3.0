/** 
 * JS for page actions in add activity page 
 **/

$(document).ready(function() {

    /**********************************************************************
     * CONSTANTS
    **********************************************************************/
    var selectActivity = null;
    var selectSiteid = null;
    var selectTech = null;
    var selectBand = null;
    var textFieldsHidden = false;
    var tableCleared = false;
    var deviceData = null;
    var cellData = null;
    var trxData = null;
    const TECH_LIST = {'2G': '2G', '3G': '3G', 'FD-LTE': 'FD-LTE', 'TD-LTE': 'TD-LTE', '5G': '5G'}
    const DEVICE_FIELD_MAP = {'device_name': 'device_id', 'vendor': 'vendor_id', 'homing': 'parent_device_id', 'equipment_type': 'model'}
    const CELL_FIELD_MAP = {
        '2G':       {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'sac_ci_eutra', 'lac': 'lac_tac', 'trx_config': '', 'bandwidth': '',},
        '3G':       {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'rnc_cid', 'lac': 'lac_tac', 'sac': 'sac_ci_eutra', 'iub_type': '', 'bandwidth': '',},
        'FD-LTE':   {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'sac_ci_eutra', 'lac': 'lac_tac', 'pci': 'phy_cid', 'bandwidth': '', 'omip': '', 's1_c': '', 's1_u': '',},
        'TD-LTE':   {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'sac_ci_eutra', 'lac': 'lac_tac', 'pci': 'phy_cid', 'bandwidth': '', 'omip': '', 's1_c': '', 's1_u': '',},
        '5G':       {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'sac_ci_eutra', 'lac': 'lac_tac', 'pci': 'phy_cid', 'bandwidth': '', 'omip': '', 's1_c': '', 's1_u': '',},
    }
    const NMS_SRC_ACTIVITY = {
        'Device': ['Rollout'],
        'Cell': ['Rollout', 'Expansion'],
        'Trx': ['Rollout', 'Expansion', 'TRX Expansion']
    }
    
    /**********************************************************************
     * Functions
    **********************************************************************/
    function reset_activity_logger_form(){
        $('#activity-logger-form')[0].reset();
    }

    function clear_table(tableId){
        if($.fn.dataTable.isDataTable(tableId)){
            $(tableId).DataTable().clear().destroy();
            $(`${tableId}-container`).hide();
            $(`${tableId}-separator`).hide();
        }
    }

    function clear_tables(){
        if(!tableCleared){
            tables = ['#filtered-device-table', '#filtered-cell-table'];
            for(let i=0; i<tables.length; i++){
                if($.fn.DataTable.isDataTable(tables[i])){
                    $(tables[i]).DataTable().clear().destroy();
                }
            }
            $('.datatable-container').hide();
            $('.dt-separator').hide();
            tableCleared = true;
        }
    }

    function disable_stb_select_fields(){
        $('#activity-logger-form *').filter(':input').each(function(){
            if(this.type != 'hidden' &&  
                (this.name == 'siteid' || this.name == 'tech' || this.name == 'band')){
                $(this).prop("disabled", true);
            }
        });
    }

    function hide_text_field_containers(){
        if(!textFieldsHidden){
            $('#activity-logger-form *').filter('.tf-container').each(function(){
                let field_name = $(this).find('label').attr('for');
                $(this).attr('id', `${field_name}_field_container`);
                $(`#${field_name}_field_container :input`).prop('required', false).val('');
                $(this).hide();
            });
            textFieldsHidden = true;
        }
    }

    function hide_text_fields(fieldMap){
        if(!textFieldsHidden){
            for(item in fieldMap){
                if(fieldMap[item].constructor == Object){
                    for(field in fieldMap[item]){
                        $(`#${field}_field_container`).hide();
                        $(`#id_${field}`).val('');
                    }
                }else{
                    $(`#${item}_field_container`).hide();
                    $(`#id_${item}`).val('');
                }
            }
        }
    }

    function hide_general_input_container(){
        $('.general-input-container').hide();
        $('.general-input-container :input').val('');
    }

    function show_general_input_container(){
        if(selectActivity == 'Rollout'){
            $("#id_site_status option").filter(function() {
                //may want to use $.trim in here
                return $(this).text() == 'Unlocked';
            }).prop('selected', true);
        }

        $('#id_user option').filter(function(){
            return $(this).text() == Cookies.get('aid-user');
        }).prop('selected', true);

        $('.general-input-container').show();
    }

    function draw_datatable(tableId, dataTableOptions){
        clear_table(tableId);
        dataTable=$(tableId).DataTable(dataTableOptions);
        $(`${tableId}-container`).show();
        $(`${tableId}-separator`).show();
        tableCleared = false;
    }

    function revise_table_option(tech, options){
        switch(tech){
            case TECH_LIST['2G']:
                /**
                options['initComplete'] = function(settings, json){
                    cellData = json.data;
                    //fill_to_form_fields(cellData, CELL_FIELD_MAP[selectTech]);
                    console.log(cellData);
                    if(cellData.length > 0){
                        show_general_input_container();
                        cellIDs = concat_unique_multiple_values(cellData.map(item => item.id))
                        draw_trx_datatable(cellIDs);
                    }else{
                        $('#concat-ne-id').html(`(${selectSiteid}-${selectTech}-${selectBand})`);
                        $('#ne-not-found-modal').modal('show');
                    }
                }
                */
                break;
            case TECH_LIST['3G']:
                options['columns'][8]['data'] = 'rnc_cid';
                options['columns'][10]['data'] = 'sac_ci_eutra';
                options['columnDefs'][8]['name'] = 'rnc_cid';
                options['columnDefs'][10]['name'] = 'sac_ci_eutra';
                break;
            case TECH_LIST['FD-LTE']:
                break;
            case TECH_LIST['TD-LTE']:
                break;
            case TECH_LIST['5G']:
                break;
            default:
        }

        return options;
    }

    function draw_device_datatable(siteid, tech, device_rec_id = null){
        var list_of_activity_where_src_is_nms = NMS_SRC_ACTIVITY['Device'];
        var options = {
            processing: true,
            serverSide: true,
            select: true,
            ajax: device_url_selector(),
            columns: [
                {data: 'ems_id'},
                {data: 'dn'},
                {data: 'device_id'},
                {data: 'parent_device_id'},
                {data: 'ne_type'},
                {data: 'record_status'},
                {data: 'site_id'},
                {data: 'subdomain'},
                {data: 'vendor_id'},
                {data: 'domain'},
                {data: 'model'},
                {data: 'id'},
            ],
            columnDefs: [
                {name: 'ems_id', searchable: true, targets: [0]},
                {name: 'dn', searchable: false, visible: false,  targets: [1]},
                {name: 'device_id', searchable: true, targets: [2]},
                {name: 'parent_device_id', searchable: true, targets: [3]},
                {name: 'ne_type', searchable: true, targets: [4]},
                {name: 'record_status', searchable: false, targets: [5]},
                {name: 'site_id', searchable: false, visible: false, targets: [6]},
                {name: 'subdomain', searchable: false, visible: false, targets: [7]},
                {name: 'vendor_id', searchable: false, visible: false,  targets: [8]},
                {name: 'domain', searchable: false, visible: false, targets: [9]},
                {name: 'model', searchable: false, visible: false, targets: [10]},
                {name: 'id', searchable: false, visible: false, targets: [11]},
            ],
            searchCols: [ 
                null, null, null, null, null, 
                {'search': siteid}, {'search': tech}, null, null, null, 
                null, 
            ],
            order: [[2,'asc']],
            dom: 'ltipr',
            language: {
                processing: 'Loading. Please wait...'
            },
            'initComplete': function(settings, json){
                //fill_device_data_to_form_fields(json.data);
                deviceData = json.data;
                fill_to_form_fields(deviceData, DEVICE_FIELD_MAP);
                console.log(deviceData);
            }
        }

        if(device_rec_id){
            options['searchCols'] = [
                null, null, null, null, null, 
                null, null, null, null, null, 
                null, {'search': device_rec_id}, 
            ]
        }

        function device_url_selector(){
            let url = '/edrar/data/datatable/device/aid/';
            if(list_of_activity_where_src_is_nms.includes(selectActivity)){
                url = '/edrar/data/datatable/device/nms/';
            }
            return url
        }
        draw_datatable('#filtered-device-table', options);
    }

    function draw_cell_datatable(siteid, tech, band){
        var list_of_activity_where_src_is_nms = NMS_SRC_ACTIVITY['Cell'];
        var src = null;
        var options = {
            processing: true,
            serverSide: true,
            select: true,
            ajax: cell_url_selector(),
            columns: [
                {data: 'ems_id'},
                {data: 'cell_name'},
                {data: 'parent_id'},
                {data: 'parent_dn'},
                {data: 'band'},
                {data: 'ne_type'},
                {data: 'nodeid'},
                {data: 'lac_tac'},
                {data: 'sac_ci_eutra'},
                {data: 'record_status'},
                {data: 'rnc_cid'},
                {data: 'phy_cid'},
                {data: 'domain'},
                {data: 'site'},
                {data: 'subdomain'},
                {data: 'id'},
            ],
            columnDefs: [
                {name: 'ems_id', searchable: true, targets: [0]},
                {name: 'cell_name', searchable: true, targets: [1]},
                {name: 'parent_id', searchable: true, targets: [2]},
                {name: 'parent_dn', searchable: false, visible: false, targets: [3]},
                {name: 'band', searchable: true, targets: [4]},
                {name: 'ne_type', searchable: true, targets: [5]},
                {name: 'nodeid', searchable: true, targets: [6]},
                {name: 'lac_tac', searchable: true, targets: [7]},
                {name: 'sac_ci_eutra', searchable: true, targets: [8]},
                {name: 'record_status', searchable: false, targets: [9]},
                {name: 'rnc_cid', searchable: false, visible: false, targets: [10]},
                {name: 'phy_cid', searchable: false, visible: false, targets: [11]},
                {name: 'domain', searchable: false, visible: false, targets: [12]},
                {name: 'site', searchable: false, visible: false, targets: [13]},
                {name: 'subdomain', searchable: false, visible: false, targets: [14]},
                {name: 'id', searchable: false, visible: false, targets: [15]},
            ],
            searchCols: [ 
                null, null, null, null, {'search': band},
                null, null, null, null, null, null, 
                null, null, {'search': siteid}, {'search': tech}, null,
            ],
            order: [[1,'asc']],
            dom: 'fltipr',
            language: {
                processing: 'Loading. Please wait...'
            },
            'initComplete': function(settings, json){
                cellData = json.data;
                //fill_to_form_fields(cellData, CELL_FIELD_MAP[selectTech]);
                if(cellData.length > 0){
                    show_general_input_container();
                    console.log(cellData);
                }else{
                    $('#concat-ne-id').html(`(${selectSiteid}-${selectTech}-${selectBand})`);
                    $('#ne-not-found-modal').modal('show');
                }
            }
        }

        function cell_url_selector(){
            let url = '/edrar/data/datatable/cell/aid/';
            if(list_of_activity_where_src_is_nms.includes(selectActivity)){
                url = '/edrar/data/datatable/cell/nms/';
                src = 'nms'
            }
            return url
        }

        options = revise_table_option(tech, options);
        draw_datatable('#filtered-cell-table', options);
        get_full_ne_data(siteid, tech, band, src);
    }

    function draw_trx_datatable(trx_rec_ids){
        var list_of_activity_where_src_is_nms = NMS_SRC_ACTIVITY['Trx'];
        var options = {
            processing: true,
            serverSide: true,
            select: true,
            ajax: trx_url_selector(),
            columns: [
                {data: 'ems_id'},
                {data: 'trx_name'},
                {data: 'parent_id'},
                {data: 'homing_bts'},
                {data: 'e1_assignment'},
                {data: 'admin_state'},
                {data: 'cell'},
                {data: 'id'},
            ],
            columnDefs: [
                {name: 'ems_id', searchable: true, visible: false, targets: [0]},
                {name: 'trx_name', searchable: true, targets: [1]},
                {name: 'parent_id', searchable: true, targets: [2]},
                {name: 'homing_bts', searchable: true, targets: [3]},
                {name: 'e1_assignment', searchable: true, targets: [4]},
                {name: 'admin_state', searchable: true, targets: [5]},
                {name: 'cell', searchable: false, visible: false, targets: [6]},
                {name: 'id', searchable: false, visible: false, targets: [7]},
            ],
            order: [[2,'asc']],
            searchCols: [ 
                null, null, null, 
                null, null, null, 
                null, {'search': trx_rec_ids},
            ],
            dom: 'fltipr',
            language: {
                processing: 'Loading. Please wait...'
            },
            'initComplete': function(settings, json){
                trxData = json.data;
                fill_trx_config_field();
                console.log(trxData);
            }
        }

        function trx_url_selector(){
            let url = '/edrar/data/datatable/trx/aid/';
            if(list_of_activity_where_src_is_nms.includes(selectActivity)){
                url = '/edrar/data/datatable/trx/nms/';
            }
            return url
        }

        draw_datatable('#filtered-trx-table', options);
    }

    function verify_device_data(data){
        uniq_device_dict = {}
        device_data = Object.values(data).map(cell => cell.device);
        for(i in device_data){
            if(Array.isArray(device_data[i])){
                for(j in device_data[i]){
                    uniq_device_dict[device_data[i][j].id] = device_data[i][j].device_id;
                }
            }else{
                uniq_device_dict[device_data[i].id] = device_data[i].device_id;
            }
        }

        let redraw_device_table = compare_datatable_v_device_data(uniq_device_dict);

        search_ids = Object.keys(uniq_device_dict).map(id => id).join(';');
        if(redraw_device_table) draw_device_datatable(null, null, search_ids);
    }

    function compare_datatable_v_device_data(uniq_device_id_dict){
        redraw_device_tbl = false;
        if($.fn.dataTable.isDataTable('#filtered-device-table')){
            datatable = $('#filtered-device-table').DataTable();
            if(datatable.data().any()){
                device_rec_ids = Object.keys(uniq_device_id_dict);
                datatable_device_data = Object.values(datatable.rows().data()).filter(device => device.id);
                datatable_device_row_ids = Object.values(datatable_device_data).map(device => device.id);
                for(i in device_rec_ids){
                    foundIndex = datatable_device_row_ids.indexOf(device_rec_ids[i]);
                    if(foundIndex > -1){
                        datatable_device_row_ids.splice(foundIndex, 1)
                    }
                }

                if(datatable_device_row_ids.length > 0){
                    redraw_device_tbl = true;
                }
            }else{
                redraw_device_tbl = true;
            }
        }

        return redraw_device_tbl;
    }

    function get_full_ne_data(siteid, tech, band, src){
        cells_data = null;
        $.ajax({
            type: "GET",
            url: '/edrar/data/tfdata/',
            data: {
                'site': siteid,
                'tech': tech,
                'band': band,
                'src': src
            },
            cache: false,
            success: function(json, status){
                if(status == 'success'){
                    //verify_device_data(json.results);
                    cells_data = json.results
                }
            },
            error: function(xhr, status, error){
                console.log(`${status}: ${error}`);
                alert('Unexpected error occured. Contact administrator.');
            },
            complete: function(xhr, status){
                if(status == 'success' && cells_data.length > 0){
                    verify_device_data(cells_data);
                    fill_to_form_fields(cells_data, CELL_FIELD_MAP[tech]);
                    if(tech == TECH_LIST['2G']){
                        trx_data = Object.values(cells_data).map(cell => cell.trx);
                        let uniq_trx_dict = {}
                        for(i in trx_data){
                            if(Array.isArray(trx_data[i])){
                                for(j in trx_data[i]){
                                    uniq_trx_dict[trx_data[i][j].id] = trx_data[i][j].trx_name;
                                }
                            }else{
                                uniq_trx_dict[trx_data[i].id] = trx_data[i].trx_name;
                            }
                        }
                        let search_ids = Object.keys(uniq_trx_dict).map(id => id).join(';');
                        if(search_ids != ''){
                            draw_trx_datatable(search_ids);
                        }else{
                            $('#no-trx-found-modal').modal('show');
                        }
                    }
                }
            }
        });
    }

    function concat_unique_multiple_values(dataArray){
        //remove duplicate
        uniqDataArray = dataArray.filter((value,index,arr)=>arr.indexOf(value)===index);
        //remove empty
        uniqDataArray = uniqDataArray.filter(value => value);
        return uniqDataArray.join(';');
    }

    function fill_to_form_fields(data, inputFieldMap){
        //let input_field_map = {'device_name': 'device_id', 'vendor': 'vendor_id', 'homing': 'parent_device_id', 'equipment_type': 'model'};
        if(data.length == 1){
            Object.keys(inputFieldMap).map(field => $(`#id_${field}`).prop('required', true)
                .val(data[0][inputFieldMap[field]]));
        }else if(data.length > 1){
            Object.keys(inputFieldMap).map(field => $(`#id_${field}`).prop('required', true)
                .val(concat_unique_multiple_values(data.map(row => row[inputFieldMap[field]]))));
        }
        Object.keys(inputFieldMap).map(field => $(`#${field}_field_container`).show());
        textFieldsHidden = false;
    }

    function fill_trx_config_field(){
        trxParentDictCount = {};
        trxParentDict = Object.values(trxData).map(item => item.parent_id);
        for(i in trxParentDict){
            if(trxParentDict[i] in trxParentDictCount){
                trxParentDictCount[trxParentDict[i]] += 1;
            }else{
                trxParentDictCount[trxParentDict[i]] = 1;
            }
        }

        trxConfig = Object.values(trxParentDictCount).map(trxCount => trxCount).join('+');
        $('#id_trx_config').val(trxConfig);
    }
    


    /**********************************************************************
     * Page Events
    **********************************************************************/
    

    $('#id_activity').on('change', function(){
        selectActivity = $('#id_activity').val() ? $('#id_activity').find(':selected').text() : null;
        if(selectActivity){
            $('select.select2').prop("disabled", false);
        }else{
            reset_activity_logger_form();
            disable_stb_select_fields();
            clear_tables();
            hide_text_field_containers();
        }
    });

    $('#id_siteid').on('change', function(){
        selectSiteid = $('#id_siteid').val() ? $('#id_siteid').find(':selected').text() : null;
        $('#id_tech').val(null).trigger('change');

        deviceData = null;
        cellData = null;
        trxData = null;

        if(selectSiteid && selectTech){
            draw_device_datatable(selectSiteid, selectTech);
        }else{
            hide_text_field_containers();
            hide_general_input_container();
            clear_tables();
        }
    });

    $('#id_tech').on('change', function(){
        selectTech = $('#id_tech').val() ? $('#id_tech').find(':selected').text() : null;
        $('#id_band').val(null).trigger('change');

        deviceData = null;
        cellData = null;
        trxData = null;

        if(selectSiteid && selectTech){
            draw_device_datatable(selectSiteid, selectTech);
        }else{
            hide_text_field_containers();
            hide_general_input_container();
            clear_tables();
        }
    });

    $('#id_band').on('change', function(){
        selectBand = $('#id_band').val() ? $('#id_band').find(':selected').text() : null;

        cellData = null;
        trxData = null;

        if(selectSiteid && selectTech && selectBand){
            Object.keys(CELL_FIELD_MAP[selectTech]).map(field => $(`id_${field}`).val(''));
            if(selectTech == TECH_LIST['2G']){
                clear_table('#filtered-trx-table');
            }
            draw_cell_datatable(selectSiteid, selectTech, selectBand);
        }else{
            hide_text_fields(CELL_FIELD_MAP);
            hide_general_input_container();
            clear_table('#filtered-cell-table');
            clear_table('#filtered-trx-table');
        }
    });

    $('#ne-not-found-modal').on('hidden.bs.modal', function(){
        $('#concat-ne-id').html('');
    })

    /**********************************************************************
     * ON PAGE LOAD TRIGGERS
    **********************************************************************/
    $('#id_activity').select2({
        placeholder: 'Select Activity',
        ajax: {
        url: "/edrar/data/select2/activity-autocomplete/",
        dataType: 'json',
        }
    });
    
    $('#id_siteid').select2({
        placeholder: 'Select Site',
        ajax: {
            url: "/edrar/data/select2/siteid-autocomplete/",
            dataType: 'json',
        }
    });

    $('#id_tech').select2({
        placeholder: 'Select Tech',
        ajax: {
            url: "/edrar/data/select2/mobiletech-autocomplete/",
            dataType: 'json',
        }
    });

    $('#id_band').select2({
        placeholder: 'Select Freq Band',
        ajax: {
            url: "/edrar/data/select2/mobilefreqband-autocomplete/",
            dataType: 'json',
        }
    });


    disable_stb_select_fields();
    clear_tables();
    hide_text_field_containers();
    hide_general_input_container();
});