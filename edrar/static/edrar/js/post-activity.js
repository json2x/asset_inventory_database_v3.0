/** 
 * JS for saving logged activity 
 **/

 $(document).ready(function() {
    var Devices = [];
    var Cells = [];
    var Trxs = [];
    var LoggedActivity = null;
    /**********************************************************************
     * OBJECTS
    **********************************************************************/
    function Device(){
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
        this.cluster_region = null;
        this.cluster_sub_region = null;
        this.cluster_province = null;
        this.cluster_city = null;
        this.mw_hub = null;
        this.record_status = null;
    }

    function Cell(){
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
        this.azimuth = null;
        this.record_status = null;
        this.device = null;
    }

    function Trx(){
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
        this.record_status = null;
        this.cell = null;
        this.device = null;
    }

    function Activity(){
        this.date_logged = null;
        this.tech = null;
        this.user = null;
        this.counterpart = null;
        this.activity = null;
        this.site_status = null;
        this.rfs_count = null;
        this.siteid = null;
        this.band = null;
        this.vendor = null;
        this.homing = null;
        this.bts_id = null;
        this.device_name = null;
        this.equipment_type = null;
        this.trx_config = null;
        this.iub_type = null;
        this.bandwidth = null;
        this.sac = null;
        this.cell_id = null;
        this.cell_name = null;
        this.lac = null;
        this.pci = null;
        this.omip = null;
        this.s1_c = null;
        this.s1_u = null;
        this.remarks = null;
        this.modified = null;
    }
    

    /**********************************************************************
     * Functions
    **********************************************************************/
    Device.prototype.save = function(){
        save_record(this, 'Device');
    }

    Cell.prototype.save = function(){
        save_record(this, 'Cell');
    }

    Trx.prototype.save = function(){
        save_record(this, 'Trx');
    }

    Activity.prototype.save = function(){
        save_record(this, 'DailyActivity');
    }

    function save_record(Obj, table){
        console.log(Obj);
        //for(var [key, val] of Object.entries(Obj)){
        //    console.log(`${key}: ${val}`);
        //}
    }

    function instantiateObject(data, Obj, GlobalVar){
        for(i in data){
            GlobalVar[i] = new Obj();
            for(let [key, val] of Object.entries(data[i])){
                GlobalVar[i][key] = val;
            }
        }
        //console.log(Devices);
    }

    async function get_device_data_by_id(){
        const device_data = $('#filtered-device-table').DataTable().rows().data();
        const ids = device_data.map(item => item.id).join(';');
        const response = await fetch(`/edrar/data/device/?id=${ids}`, {
            method: 'GET',
            cache: 'no-cache',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        return device = response.json();
    }

    async function get_cell_data_by_id(){
        const device_data = $('#filtered-cell-table').DataTable().rows().data();
        const ids = device_data.map(item => item.id).join(';');
        const response = await fetch(`/edrar/data/cell/?id=${ids}`, {
            method: 'GET',
            cache: 'no-cache',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        return device = response.json();
    }

    async function get_trx_data_by_id(){
        const device_data = $('#filtered-trx-table').DataTable().rows().data();
        const ids = device_data.map(item => item.id).join(';');
        const response = await fetch(`/edrar/data/trx/?id=${ids}`, {
            method: 'GET',
            cache: 'no-cache',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        return device = response.json();
    }

    async function get_datatables_data(){
        await get_device_data_by_id().then(data => instantiateObject(data.results, Device, Devices)).catch(e => console.log(e));
        await get_cell_data_by_id().then(data => instantiateObject(data.results, Cell, Cells)).catch(e => console.log(e));
        if($.fn.dataTable.isDataTable('#filtered-trx-table')){
            await get_trx_data_by_id().then(data => instantiateObject(data.results, Trx, Trxs)).catch(e => console.log(e));
        }
    }

    async function get_jwt_token(){
        const token = await fetch('/api/user/token/');
        return token.json();
    }

    function set_jwt_token_cookie(){
        get_jwt_token().then(function(result){
            Cookies.set('aid-user', result.user,  {expires: 1});
            Cookies.set('aid-token-access', result.access,  {expires: 1});
            Cookies.set('aid-token-refresh', result.refresh,  {expires: 1});
            
            console.log(Cookies.get('aid-user'));
            console.log(Cookies.get('aid-token-access'));
            console.log(Cookies.get('aid-token-refresh'));
        }).catch((e) => console.log(e));
    }


    /**********************************************************************
     * Events
    **********************************************************************/
    var loading_html = $('#confirm-activity').html();
    $('#save-activity').click(function(e){
        console.log(NE_DATA);
        $('#confirm-activity').prop('disabled', true);
        let show_confirm_modal = true;
        LoggedActivity = new Activity();
        $('#activity-logger-form *').filter(':input[required]').each(function(){
            let propertyName = ($(this).attr('id')).replace('id_', '');
            if($(this).is('select')){
                LoggedActivity[propertyName] = $(this).find(':selected').text();
            }else{
                LoggedActivity[propertyName] = $(this).val();
            }
            
            if(!LoggedActivity[propertyName]){
                 show_confirm_modal = false;
             }
        });

        if(show_confirm_modal){
            e.preventDefault();
            get_datatables_data().then(function(){
                console.log(Devices);
                console.log(Cells);
                console.log(Trxs);
                $('#confirm-activity').html('Confirm');
                $('#confirm-activity').prop('disabled', false);
            }).catch(function(e){
                console.log(e);
            });
            //Promise.all([Devices, Cells, Trxs]).then(console.log([Devices, Cells, Trxs]));
            $('#confirm-save-modal').modal('show');
        }
    });

    $('#confirm-activity').click(function(e){
        e.preventDefault();
        $(this).html(loading_html);
        let to_save_list = [Devices, Cells, Trxs];

        for(i in to_save_list){
            for(let j in to_save_list[i]){
                let obj = to_save_list[i][j]
                obj.save();
            }
        }

        $(this).html('Completed');
    });


    /**********************************************************************
     * ON PAGE LOAD TRIGGERS
    **********************************************************************/

    if (!Cookies.get('aid-user') && !Cookies.get('aid-token-access') && !Cookies.get('aid-token-refresh')) {
        set_jwt_token_cookie();
    }else{
        let logged_user = $('#user-name').html();
        if(Cookies.get('aid-user') != logged_user){
            set_jwt_token_cookie();
        }
    }
    

    /**********************************************************************
     * Tests
    **********************************************************************/
    //Site101 = new Device('101');
    //Site101.save();

    //Site102 = new Cell('102');
    //Site102.save();

    //Site103 = new Trx('103');
    //Site102.save();
 });