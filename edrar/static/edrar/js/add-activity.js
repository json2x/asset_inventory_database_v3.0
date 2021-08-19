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

    function reset_selected_tables(){
        $('#device-selected-table').hide();
    }

    function disable_input_fields(){
        $('#activity-logger-form *').filter(':input').each(function(){
            if(this.type != 'hidden' &&  this.name != 'activity'){
                $(this).prop("disabled", true);
            }
        });
    }

    function destroy_datatable(domSelector){
        table=$(domSelector).DataTable();
        table.destroy();
    }

    function concat_unique_multiple_values(dataArray){
        uniqDataArray = dataArray.filter((v,i,a)=>a.indexOf(v)===i);
        return uniqDataArray.join('|')
    }

    function fill_device_data_to_form_fields(data){
        if(data.length > 1){
            $('#id_device_name').prop("disabled", false);

            $('#id_device_name').val( concat_unique_multiple_values( (() => {let dataArray = []; for(let i=0; i<data.length; i++){dataArray.push(data[i]['device_id'])} return dataArray; })() ) );
            $('#id_tech').val( concat_unique_multiple_values( (() => {let dataArray = []; for(let i=0; i<data.length; i++){dataArray.push(data[i]['subdomain'])} return dataArray; })() ) );
            $('#id_vendor').val( concat_unique_multiple_values( (() => {let dataArray = []; for(let i=0; i<data.length; i++){dataArray.push(data[i]['vendor_id'])} return dataArray; })() ) );
            $('#id_homing').val( concat_unique_multiple_values( (() => {let dataArray = []; for(let i=0; i<data.length; i++){dataArray.push(data[i]['parent_device_id'])} return dataArray; })() ) );
            $('#id_equipment_type').val( concat_unique_multiple_values( (() => {let dataArray = []; for(let i=0; i<data.length; i++){dataArray.push(data[i]['model'])} return dataArray; })() ) );
        }else{
            $('#id_device_name').prop("disabled", false);

            $('#id_device_name').val(data[0]['device_id']);
            $('#id_tech').val(data[0]['subdomain']);
            $('#id_vendor').val(data[0]['vendor_id']);
            $('#id_homing').val(data[0]['parent_device_id']);
            $('#id_equipment_type').val(data[0]['model']);
        }
    }

    function draw_device_datatable(siteid){
        options = {
            processing: true,
            serverSide: true,
            select: true,
            ajax: '/edrar/data/device/',
            columns: [
                {data: 'device_id'},
                {data: 'site_id'},
                {data: 'ems_id'},
                {data: 'vendor_id'},
                {data: 'parent_device_id'},
                {data: 'ne_type'},
                {data: 'subdomain'},
                {data: 'domain'},
                {data: 'model'},
            ],
            columnDefs: [
                {name: 'device_id', searchable: false, targets: [0]},
                {name: 'site_id', searchable: true, targets: [1]},
                {name: 'ems_id', searchable: false, targets: [2]},
                {name: 'vendor_id', searchable: false, targets: [3]},
                {name: 'parent_device_id', searchable: false, targets: [4]},
                {name: 'ne_type', searchable: false, targets: [5]},
                {name: 'subdomain', searchable: false, targets: [6]},
                {name: 'domain', searchable: false, targets: [7]},
                {name: 'model', searchable: false, visible: false, targets: [8]},
            ],
            search: {
                'search': siteid
            },
            dom: 'ltipr',
        }

        table=$('#aid-device-search-table').DataTable(options);
    }

    function draw_cell_datatable(tech, deviceName){
        options = {
            processing: true,
            serverSide: true,
            select: true,
            ajax: '/edrar/data/cell/',
            columns: [
                {data: 'domain'},
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
                {name: 'domain', searchable: false, targets: [0]},
                {name: 'cell_name', searchable: false, targets: [1]},
                {name: 'parent_id', searchable: true, targets: [2]},
                {name: 'site', searchable: false, targets: [3]},
                {name: 'subdomain', searchable: false, targets: [4]},
                {name: 'band', searchable: true, targets: [5]},
                {name: 'ne_type', searchable: false, targets: [6]},
                {name: 'lac_tac', searchable: false, targets: [7]},
                {name: 'sac_ci_eutra', searchable: false, targets: [8]},
            ],
            searchCols: [ 
                null, null, {'search': deviceName}, null,
                {'search': tech}, null, null, null, 
                null, null,
            ],
            oLanguage: {
                sSearch: 'Search Band:'
            },
            dom: 'fltipr',
        }

        table=$('#aid-cell-search-table').DataTable(options);
    }


    /**********************************************************************
     * Page Events
    **********************************************************************/
    $('#id_activity').change(function(){
        if($(this).val()){
            $('select.select2').prop("disabled", false);
        }else{
            $('.select2').val(null).trigger('change');
            reset_activity_logger_form();
            disable_input_fields();
            reset_selected_tables();
        }
    });

    $('.select2').on("select2:select", function(e){
        $("#device-search").prop("disabled", false);
    });

    $("#device-search").click(function(e){
        e.preventDefault();
    });
    $("#cell-search").click(function(e){
        e.preventDefault();
    });
    

    /**$('#aid-device-search-table tbody').on('dblclick','tr',function(e){
        dataTable = $('#aid-device-search-table').DataTable();
        data = dataTable.row(this).data();
        
        $('#id_device_name').prop("disabled", false).val(data[0]);
        $('#id_tech').prop("disabled", false).val(data[6]);
        $('#id_vendor').prop("disabled", false).val(data[3]);
        $('#id_homing').prop("disabled", false).val(data[4]);
        $('#id_equipment_type').prop("disabled", false).val(data[8]);

        $('#device-search-modal').modal('hide');
    });**/

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

    //when device search modal shows
    $('#device-search-modal').on('show.bs.modal', function(e){
        siteid = $('.select2').find(':selected').text();
        draw_device_datatable(siteid);
        /**
        table=$('#aid-device-search-table').DataTable({
            processing: true,
            serverSide: true,
            select: true,
            ajax: '/edrar/data/device/',
            columns: [
                {data: 'device_id'},
                {data: 'site_id'},
                {data: 'ems_id'},
                {data: 'vendor_id'},
                {data: 'parent_device_id'},
                {data: 'ne_type'},
                {data: 'subdomain'},
                {data: 'domain'},
                {data: 'model'},
            ],
            columnDefs: [
                {name: 'device_id', searchable: false, targets: [0]},
                {name: 'site_id', searchable: true, targets: [1]},
                {name: 'ems_id', searchable: false, targets: [2]},
                {name: 'vendor_id', searchable: false, targets: [3]},
                {name: 'parent_device_id', searchable: false, targets: [4]},
                {name: 'ne_type', searchable: false, targets: [5]},
                {name: 'subdomain', searchable: false, targets: [6]},
                {name: 'domain', searchable: false, targets: [7]},
                {name: 'model', searchable: false, visible: false, targets: [8]},
            ],
            dom: 'ltipr',
            search: {
                'search': siteid
            }
        });
         */
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
        /**
        table=$('#aid-cell-search-table').DataTable({
            processing: true,
            serverSide: true,
            select: true,
            ajax: '/edrar/data/cell/',
            columns: [
                {data: 'domain'},
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
                {name: 'domain', searchable: false, targets: [0]},
                {name: 'cell_name', searchable: false, targets: [1]},
                {name: 'parent_id', searchable: true, targets: [2]},
                {name: 'site', searchable: false, targets: [3]},
                {name: 'subdomain', searchable: false, targets: [4]},
                {name: 'band', searchable: true, targets: [5]},
                {name: 'ne_type', searchable: false, targets: [6]},
                {name: 'lac_tac', searchable: false, targets: [7]},
                {name: 'sac_ci_eutra', searchable: false, targets: [8]},
            ],
            dom: 'fltipr',
            searchCols: [
                null,
                null,
                {'search': deviceName, 'regex': true},
                null,
                {'search': tech},
                null,
                null,
                null,
                null,
                null,
            ],
            oLanguage: {
                sSearch: 'Search Band:'
            }
        });
         */
    });

    $('#cell-search-modal').on('hidden.bs.modal', function(e){
        destroy_datatable('#aid-cell-search-table');
    });
    

    /**********************************************************************
     * ON PAGE LOAD TRIGGERS
    **********************************************************************/
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
    reset_selected_tables();
});