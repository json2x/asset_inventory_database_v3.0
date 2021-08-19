/** 
 * JS for page actions in add activity page 
 **/

$(document).ready(function() {
    
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
        tables = ['#filtered-device-table', '#filtered-cell-table'];
        for(let i=0; i<tables.length; i++){
            if($.fn.DataTable.isDataTable(tables[i])){
                $(tables[i]).DataTable().destroy();
            }
        }
        $('.datatable-container').hide();
        $('.dt-separator').hide();
    }

    

    function disable_input_fields(){
        $('#activity-logger-form *').filter(':input').each(function(){
            if(this.type != 'hidden' &&  this.name != 'activity'){
                $(this).prop("disabled", true);
            }
        });
    }

    function draw_datatable(tableId, dataTableOptions){
        clear_table(tableId);
        dataTable=$(tableId).DataTable(dataTableOptions);
        $(`${tableId}-container`).show();
        $(`${tableId}-separator`).show();
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
                fill_device_data_to_form_fields(json.data);
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
            ],
            searchCols: [ 
                null, null, null, null, null,
                {'search': siteid}, {'search': tech}, {'search': band}, 
                null, null, null,
            ],
            dom: 'fltipr',
            'initComplete': function(settings, json){
                fill_cell_data_to_form_fields(json.data);
                console.log(json.data);
            }
        }

        draw_datatable('#filtered-cell-table', options);
    }

    function concat_unique_multiple_values(dataArray){
        //remove duplicate
        uniqDataArray = dataArray.filter((value,index,arr)=>arr.indexOf(value)===index);
        //remove empty
        uniqDataArray = uniqDataArray.filter(value => value);
        return uniqDataArray.join(';');
    }

    function fill_device_data_to_form_fields(data){
        if(data.length == 1){
            $('#id_device_name').prop("disabled", false).val(data[0]['device_id']);
            $('#id_vendor').prop("disabled", false).val(data[0]['vendor_id']);
            $('#id_homing').prop("disabled", false).val(data[0]['parent_device_id']);
            $('#id_equipment_type').prop("disabled", false).val(data[0]['model']);
        }else if(data.length > 1){
            $('#id_device_name').prop("disabled", false).val(concat_unique_multiple_values(data.map(row => row.device_id)));
            $('#id_vendor').prop("disabled", false).val(concat_unique_multiple_values(data.map(row => row.vendor_id)));
            $('#id_homing').prop("disabled", false).val(concat_unique_multiple_values(data.map(row => row.parent_device_id)));
            $('#id_equipment_type').prop("disabled", false).val(concat_unique_multiple_values(data.map(row => row.model)));
        }
    }

    function fill_cell_data_to_form_fields(data){
        if(data.length == 1){
            $('#id_bts_id').prop("disabled", false).val(data[0]['nodeid']);
            $('#id_cell_name').prop("disabled", false).val(data[0]['cell_name']);
            $('#id_cell_id').prop("disabled", false).val(data[0]['sac_ci_eutra']);
        }else if(data.length > 1){
            $('#id_bts_id').prop("disabled", false).val(concat_unique_multiple_values(data.map(row => row.nodeid)));
            $('#id_cell_name').prop("disabled", false).val(concat_unique_multiple_values(data.map(row => row.cell_name)));
            $('#id_cell_id').prop("disabled", false).val(concat_unique_multiple_values(data.map(row => row.sac_ci_eutra)));
        }
    }


    /**********************************************************************
     * Page Events
    **********************************************************************/
    siteid = null;
    tech = null;
    band = null;

    $('#id_activity').on('change', function(){
        if($(this).val()){
            $('select.select2').prop("disabled", false);
        }else{
            reset_activity_logger_form();
            disable_input_fields();
            clear_tables();
        }
    });

    $('#id_siteid').on('change', function(){
        siteid = $('#id_siteid').val() ? $('#id_siteid').find(':selected').text() : null;
        $('#id_tech').val(null).trigger('change');

        if(siteid && tech){
            draw_device_datatable(siteid, tech);
        }else{
            clear_tables();
        }
    });

    $('#id_tech').on('change', function(){
        tech = $('#id_tech').val() ? $('#id_tech').find(':selected').text() : null;
        $('#id_band').val(null).trigger('change');

        if(siteid && tech){
            draw_device_datatable(siteid, tech);
        }else{
            clear_tables();
        }
    });

    $('#id_band').on('change', function(){
        band = $('#id_band').val() ? $('#id_band').find(':selected').text() : null;

        if(siteid && tech && band){
            draw_cell_datatable(siteid, tech, band);
        }else{
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


    disable_input_fields();
    clear_tables();


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