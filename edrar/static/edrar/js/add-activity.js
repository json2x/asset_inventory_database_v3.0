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
    const TECH_LIST = {'2G': '2G', '3G': '3G', 'FD-LTE': 'FD-LTE', 'TD-LTE': 'TD-LTE', '5G': '5G'}
    const DEVICE_FIELD_MAP = {'device_name': 'device_id', 'vendor': 'vendor_id', 'homing': 'parent_device_id', 'equipment_type': 'model'};
    const CELL_FIELD_MAP = {
        '2G':       {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'sac_ci_eutra', 'lac': 'lac_tac', 'trx_config': '', 'bandwidth': '',},
        '3G':       {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'rnc_cid', 'lac': 'lac_tac', 'sac': 'sac_ci_eutra', 'iub_type': '', 'bandwidth': '',},
        'FD-LTE':   {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'sac_ci_eutra', 'lac': 'lac_tac', 'pci': 'phy_cid', 'bandwidth': '', 'omip': '', 's1_c': '', 's1_u': '',},
        'TD-LTE':   {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'sac_ci_eutra', 'lac': 'lac_tac', 'pci': 'phy_cid', 'bandwidth': '', 'omip': '', 's1_c': '', 's1_u': '',},
        '5G':       {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'sac_ci_eutra', 'lac': 'lac_tac', 'pci': 'phy_cid', 'bandwidth': '', 'omip': '', 's1_c': '', 's1_u': '',},
    }
    
    /**********************************************************************
     * Functions
    **********************************************************************/
    function reset_activity_logger_form(){
        $('#activity-logger-form')[0].reset();
    }

    function clear_table(tableId){
        if($.fn.dataTable.isDataTable(tableId)){
            $(tableId).DataTable().destroy();
            $(`${tableId}-container`).hide();
            $(`${tableId}-separator`).hide();
        }
    }

    function clear_tables(){
        if(!tableCleared){
            tables = ['#filtered-device-table', '#filtered-cell-table'];
            for(let i=0; i<tables.length; i++){
                if($.fn.DataTable.isDataTable(tables[i])){
                    $(tables[i]).DataTable().destroy();
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
                $(this).hide();
                $(`${field_name}_field_container :input`).val('');
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
                break;
            case TECH_LIST['3G']:
                options['columns'][10]['data'] = 'rnc_cid';
                options['columns'][11]['data'] = 'sac_ci_eutra';
                options['columnDefs'][10]['name'] = 'rnc_cid';
                options['columnDefs'][11]['name'] = 'sac_ci_eutra';
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

    function draw_device_datatable(siteid, tech){
        options = {
            processing: true,
            serverSide: true,
            select: true,
            ajax: '/edrar/data/device/',
            columns: [
                {data: 'ems_id'},
                {data: 'device_id'},
                {data: 'site_id'},                
                {data: 'vendor_id'},
                {data: 'parent_device_id'},
                {data: 'ne_type'},
                {data: 'subdomain'},
                {data: 'domain'},
                {data: 'model'},
            ],
            columnDefs: [
                {name: 'ems_id', searchable: false, targets: [0]},
                {name: 'device_id', searchable: false, targets: [1]},
                {name: 'site_id', searchable: true, visible: false, targets: [2]},
                {name: 'vendor_id', searchable: false, targets: [3]},
                {name: 'parent_device_id', searchable: false, targets: [4]},
                {name: 'ne_type', searchable: false, targets: [5]},
                {name: 'subdomain', searchable: true, visible: false, targets: [6]},
                {name: 'domain', searchable: false, visible: false, targets: [7]},
                {name: 'model', searchable: false, visible: false, targets: [8]},
            ],
            searchCols: [ 
                null, null, {'search': siteid}, null, 
                null, null, {'search': tech}, null, null,
            ],
            dom: 'ltipr',
            'initComplete': function(settings, json){
                //fill_device_data_to_form_fields(json.data);
                fill_to_form_fields(json.data, DEVICE_FIELD_MAP);
                console.log(json.data);
            }
        }

        draw_datatable('#filtered-device-table', options);
    }

    function draw_cell_datatable(siteid, tech, band){
        options = {
            processing: true,
            serverSide: true,
            select: true,
            ajax: '/edrar/data/cell/',
            columns: [
                {data: 'domain'},
                {data: 'ems_id'},
                {data: 'nodeid'},
                {data: 'cell_name'},
                {data: 'parent_id'},
                {data: 'site'},
                {data: 'subdomain'},
                {data: 'band'},
                {data: 'ne_type'},
                {data: 'lac_tac'},
                {data: 'sac_ci_eutra'},
                {data: 'rnc_cid'},
                {data: 'phy_cid'},
            ],
            columnDefs: [
                {name: 'domain', searchable: false, visible: false, targets: [0]},
                {name: 'ems_id', searchable: true, targets: [1]},
                {name: 'nodeid', searchable: false, targets: [2]},
                {name: 'cell_name', searchable: true, targets: [3]},
                {name: 'parent_id', searchable: true, targets: [4]},
                {name: 'site', searchable: false, visible: false, targets: [5]},
                {name: 'subdomain', searchable: true, visible: false, targets: [6]},
                {name: 'band', searchable: true, targets: [7]},
                {name: 'ne_type', searchable: false, targets: [8]},
                {name: 'lac_tac', searchable: false, targets: [9]},
                {name: 'sac_ci_eutra', searchable: false, targets: [10]},
                {name: 'rnc_cid', searchable: false, visible: false, targets: [11]},
                {name: 'phy_cid', searchable: false, visible: false, targets: [12]},
            ],
            searchCols: [ 
                null, null, null, null, null,
                {'search': siteid}, {'search': tech}, {'search': band}, 
                null, null, null, null,
            ],
            dom: 'fltipr',
            'initComplete': function(settings, json){
                //fill_cell_data_to_form_fields(json.data);
                fill_to_form_fields(json.data, CELL_FIELD_MAP[selectTech]);
                show_general_input_container();
                console.log(json.data);
            }
        }

        options = revise_table_option(TECH_LIST['3G'], options)
        draw_datatable('#filtered-cell-table', options);
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
            Object.keys(inputFieldMap).map(field => $(`#id_${field}`).val(data[0][inputFieldMap[field]]));
        }else if(data.length > 1){
            Object.keys(inputFieldMap).map(field => $(`#id_${field}`)
                .val(concat_unique_multiple_values(data.map(row => row[inputFieldMap[field]]))));
        }
        Object.keys(inputFieldMap).map(field => $(`#${field}_field_container`).show());
        textFieldsHidden = false;
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
        
        if(selectSiteid && selectTech && selectBand){
            Object.keys(CELL_FIELD_MAP[selectTech]).map(field => $(`id_${field}`).val(''));
            draw_cell_datatable(selectSiteid, selectTech, selectBand);
        }else{
            hide_text_fields(CELL_FIELD_MAP);
            hide_general_input_container();
            clear_table('#filtered-cell-table');
        }
    });

    /**********************************************************************
     * ON PAGE LOAD TRIGGERS
    **********************************************************************/
    $('#id_activity').select2({
        placeholder: 'Select Activity',
        ajax: {
        url: "/edrar/data/activity-autocomplete/",
        dataType: 'json',
        }
    });
    
    $('#id_siteid').select2({
        placeholder: 'Select Site',
        ajax: {
            url: "/edrar/data/siteid-autocomplete/",
            dataType: 'json',
        }
    });

    $('#id_tech').select2({
        placeholder: 'Select Tech',
        ajax: {
            url: "/edrar/data/mobiletech-autocomplete/",
            dataType: 'json',
        }
    });

    $('#id_band').select2({
        placeholder: 'Select Freq Band',
        ajax: {
            url: "/edrar/data/mobilefreqband-autocomplete/",
            dataType: 'json',
        }
    });


    disable_stb_select_fields();
    clear_tables();
    hide_text_field_containers();
    hide_general_input_container();

    /*******************************************************************************************
     * *****************************************************************************************
     * DUMPED METHODS
     ******************************************************************************************
     ******************************************************************************************/

    //$('.select2').on("select2:select", function(e){
    //    $("#device-search").prop("disabled", false);
    //});

    function destroy_datatable(domSelector){
        table=$(domSelector).DataTable();
        table.destroy();
    }

    $("#device-search").click(function(e){
        e.preventDefault();
    });
    $("#cell-search").click(function(e){
        e.preventDefault();
    });

    $('#aid-device-select-rows').click(function(e){
        e.preventDefault();
        selectedData = [];
        dataTable = $('#aid-device-search-table').DataTable();
        data = dataTable.rows('.selected').data();
        for(i=0;i<data.length;i++){
            selectedData.push(data[i]);
        }
        
        fill_device_data_to_form_fields(selectedData);
        $('#device-search-modal').modal('hide');
    });
    // MODAL EVENTS
    //when device search modal shows
    $('#device-search-modal').on('show.bs.modal', function(e){
        siteid = $('.select2').find(':selected').text();
        draw_device_datatable(siteid);
    });

    //when device search modal is hidden
    $('#device-search-modal').on('hidden.bs.modal', function(e){
        destroy_datatable('#aid-device-search-table');

        if($('#id_device_name').val()){
            $("#cell-search").prop("disabled", false);
        }
    });

    $('#cell-search-modal').on('show.bs.modal', function(e){
        tech = $('#id_tech').val();
        deviceName = $('#id_device_name').val();
        draw_cell_datatable(tech, deviceName);
    });

    $('#cell-search-modal').on('hidden.bs.modal', function(e){
        destroy_datatable('#aid-cell-search-table');
    });
    // END OF MODAL EVENTS
});