/** 
 * JS for page actions in add activity page 
 **/

$(document).ready(function() {

    /**********************************************************************
     * CONSTANTS
    **********************************************************************/
    var Devices = null;
    var Cells = null;
    var Trxs = null;

    var selectSiteid = null;
    var selectTech = null;
    var selectBand = null;
    var selectActivity = null;

    const urlSearchParams = new URLSearchParams(window.location.search);
    const url_params = Object.fromEntries(urlSearchParams.entries());
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
        $('.datatable-container').hide();
        $('.dt-separator').hide();
        tables = ['#filtered-device-table', '#filtered-cell-table', '#filtered-trx-table'];
        for(i in tables){
            if($.fn.DataTable.isDataTable(tables[i])){
                $(tables[i]).DataTable().clear().destroy();
            }
            $(`${tables[i]}-container`).removeClass('d-none');
            $(`${tables[i]}-separator`).removeClass('d-none');
        }
    }

    function disable_stb_select_fields(){
        $("#save-activity").prop("disabled", true);
        $("#id_siteid").prop("disabled", true);
        $("#id_tech").prop("disabled", true);
        $("#id_band").prop("disabled", true);
    }

    function hide_text_field_containers(){
        $('#activity-logger-form *').filter('.tf-container').each(function(){
            let field_name = $(this).find('label').attr('for');
            $(this).attr('id', `${field_name}_field_container`);
            $(`#${field_name}_field_container :input`).prop('required', false).val('');
            $(this).hide();
            $(this).removeClass('d-none');
        });
    }

    function hide_general_input_container(){
         $('.general-input-container').hide();
         $('.general-input-container :input').prop('required', false).val('');
    }

    // function hide_text_fields(fieldMap){
    //     if(!textFieldsHidden){
    //         for(item in fieldMap){
    //             if(fieldMap[item].constructor == Object){
    //                 for(field in fieldMap[item]){
    //                     $(`#${field}_field_container`).hide();
    //                     $(`#id_${field}`).val('');
    //                 }
    //             }else{
    //                 $(`#${item}_field_container`).hide();
    //                 $(`#id_${item}`).val('');
    //             }
    //         }
    //     }
    // }

    // function show_general_input_container(){
    //     if(selectActivity == 'Rollout'){
    //         $("#id_site_status option").filter(function() {
    //             //may want to use $.trim in here
    //             return $(this).text() == 'Unlocked';
    //         }).prop('selected', true);
    //     }

    //     if(selectActivity == 'On-Air'){
    //         $("#id_site_status option").filter(function() {
    //             //may want to use $.trim in here
    //             return $(this).text() == 'On-air';
    //         }).prop('selected', true);
    //     }

    //     $('#id_user option').filter(function(){
    //         return $(this).text() == Cookies.get('aid-user');
    //     }).prop('selected', true);

    //     $('.general-input-container').show();
    // }

    function remove_duplicate_objects_in_array(refKeysArray, obj){
        filtered = obj.filter(
            (s => o => 
                (k => !s.has(k) && s.add(k))
                (refKeysArray.map(k => o[k]).join('|'))
            )
            (new Set)
        );

        return filtered;
    }

    function get_data_array_in_obj(obj, key){
        dataArray = [];
        for(i in obj){
            for(j in obj[i][key]){
                if(obj[i][key][j]['record_status'] < 3){
                    dataArray.push(obj[i][key][j]);
                }
            }
        }
        
        return dataArray;
    }

    function set_page_ne_data(reset_discarded_ne_data = true){
        if(selectTech == G_TECH_LIST['2G']){
            Trxs = {
                'aid': get_data_array_in_obj(G_NE_DATA['aid'], 'trx'),
                'nms': get_data_array_in_obj(G_NE_DATA['nms'], 'trx')
            }
        }
        
        Devices = {
            'aid': remove_duplicate_objects_in_array( ['id'], Object.values(G_NE_DATA['aid']).map(cell => cell.device) ),
            'nms': remove_duplicate_objects_in_array( ['id'], get_data_array_in_obj(G_NE_DATA['nms'], 'device') )
        }
        Devices['aid'] = Object.values(Devices['aid']).filter(device => device.record_status < 3);

        Cells = {
            // 'aid': Object.values(G_NE_DATA['aid']).map(cell => cell),
            'aid': Object.values(G_NE_DATA['aid']).filter(cell => cell.record_status < 3),
            'nms': Object.values(G_NE_DATA['nms']).map(cell => cell)
        }
        //reset G_DISCARD_NE_DATA
        if(reset_discarded_ne_data){
            G_DISCARDED_NE_DATA = {
                'nms': {'DEVICE': [],'CELL': [],'TRX': [],}, 
                'aid': {'DEVICE': [],'CELL': [],'TRX': [],}
            }
        }
    }

    function reset_page_ne_data(){
        set_page_ne_data(false);
    }

    function assign_relationship_ids_to_datatable_row_data(){
        for(let[src, srcObjDataArray] of Object.entries(G_NE_DATA)){
            if(srcObjDataArray.length > 0){
                rel_id = Math.random() * (i+1);
                prev = [];
                for(i in srcObjDataArray){
                    if(Array.isArray(srcObjDataArray[i]['device'])){
                        for(j in srcObjDataArray[i]['device']){
                            if(prev.indexOf(srcObjDataArray[i]['device'][j]['id']) == -1){
                                rel_id = Math.random() * (i+1);
                            }
                            srcObjDataArray[i]['device'][j]['rel_id'] = rel_id;
                        }
                        prev = srcObjDataArray[i]['device'].map(device => device.id);
                    }else{
                        if(prev.indexOf(srcObjDataArray[i]['device']['id']) == -1){
                            rel_id = Math.random() * (i+1);
                        }
                        srcObjDataArray[i]['device']['rel_id']  = rel_id;
                        prev.push(srcObjDataArray[i]['device']['id']);
                    }
                    
                    for(j in srcObjDataArray[i]['trx']){
                        srcObjDataArray[i]['trx'][j]['rel_id']  = rel_id;
                    }
                    srcObjDataArray[i]['rel_id'] = rel_id;

                }
            }
        }
    }

    function draw_datatables(){
        MyDataTable.set_info(selectActivity, selectSiteid, selectTech, selectBand);
        MyDataTable.draw_device_table(Devices);
        MyDataTable.draw_cell_table(Cells);
        if(selectTech == G_TECH_LIST['2G']){
            MyDataTable.draw_trx_table(Trxs);
        }
    }

    function draw_fill_form_fields(){
        MyActivityForm.set_info(selectActivity, selectSiteid, selectTech, selectBand);
        MyActivityForm.fill_to_form_fields(Devices, G_FIELD_MAP['DEVICE'], G_NMS_SRC_ACTIVITY['DEVICE']);
        MyActivityForm.fill_to_form_fields(Cells, G_FIELD_MAP['CELL'],  G_NMS_SRC_ACTIVITY['CELL']);
        if(selectTech == G_TECH_LIST['2G']){
            MyActivityForm.fill_trx_config_field(Trxs, G_NMS_SRC_ACTIVITY['TRX']);
        }
        MyActivityForm.fill_general_info_fields();
    }

    function update_form_fields(){
        reset_page_ne_data();
        let has_change_in_ne_data = false;
        for(let[data_src, dataObjectArray] of Object.entries(G_DISCARDED_NE_DATA)){
            for(let[tbl_src, neDataObjArray] of Object.entries(dataObjectArray)){
                switch(tbl_src){
                    case 'DEVICE':
                        remove_device_id = neDataObjArray.map(device => device.id);
                        if(remove_device_id.length > 0){
                            has_change_in_ne_data = true;
                        }
                        break;
                    case 'CELL':
                        remove_cell_id = neDataObjArray.map(cell => cell.id);
                        if(remove_cell_id.length > 0){
                            has_change_in_ne_data = true;
                        }
                        break;
                    case 'TRX':
                        remove_trx_id = neDataObjArray.map(trx => trx.id);
                        if(remove_trx_id.length > 0){
                            has_change_in_ne_data = true;
                        }
                        break;
                }
            }

            if(has_change_in_ne_data){
                Devices[data_src] = Devices[data_src].filter(function(element){
                    if(remove_device_id.indexOf(element.id) == -1){
                        return element;
                    }
                });
    
                Cells[data_src] = Cells[data_src].filter(function(element){
                    if(remove_cell_id.indexOf(element.id) == -1){
                        return element;
                    }
                });
                
                if(selectTech == G_TECH_LIST['2G']){
                    Trxs[data_src] = Trxs[data_src].filter(function(element){
                        if(remove_trx_id.indexOf(element.id) == -1){
                            return element;
                        }
                    });
                }
            }
        }

        draw_fill_form_fields();
    }

    async function get_aid_ne_data(siteid, tech, band){
        const response = await fetch(`/edrar/data/ne/?site=${siteid}&tech=${tech}&band=${band}`, {
            method: 'GET',
            cache: 'no-cache',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        return response.json();
    }

    async function get_nms_ne_data(siteid, tech, band){
        const response = await fetch(`/edrar/data/ne/?site=${siteid}&tech=${tech}&band=${band}&src=nms`, {
            method: 'GET',
            cache: 'no-cache',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        return response.json();
    }

    async function get_activity_data(url){
        const response = await fetch(url, {
            method: 'GET',
            cache: 'no-cache',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        return response.json();
    }

    async function get_bscrnc_nes(device){
        const response = await fetch(`/edrar/data/bscrnc/nes/?device_id=${device}`, {
            method: 'GET',
            cache: 'no-cache',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        return response.json();
    }

    async function get_ne_data(){
        await get_aid_ne_data(selectSiteid, selectTech, selectBand)
            .then(data => {
                G_NE_DATA['aid'] = data.results
            }).catch(e => console.log(e));
        await get_nms_ne_data(selectSiteid, selectTech, selectBand)
            .then(data => {
                G_NE_DATA['nms'] = data.results
            }).catch(e => console.log(e));
    }
    
    function render_view(){
        clear_tables();
        hide_text_field_containers();
        hide_general_input_container();

        if(selectSiteid && selectTech && selectBand){
            //$('#fetching-data-modal').modal('show');
            $('#fetching-data-modal').modal({backdrop: 'static', keyboard: false});
            if(selectTech == G_TECH_LIST['2G']){
                clear_table('#filtered-trx-table');
            }

            get_ne_data()
                .then(function(){
                    assign_relationship_ids_to_datatable_row_data();
                    set_page_ne_data();
                    draw_datatables();
                    draw_fill_form_fields();
                    $('#fetching-data-modal').modal('hide');
                    MyDataTable.evaluate_ne_info();
                    if(MyDataTable.is_ne_missing || MyDataTable.is_data_missing){
                        msg = '';
                        for(i in MyDataTable.missing_data_msg){
                            if(msg == ''){
                                msg = msg=MyDataTable.missing_data_msg[i];
                            }else{
                                msg +='<br>'+MyDataTable.missing_data_msg[i];
                            }
                        }
                        $('#missing-data-msg').html(msg);
                        $('#missing-data-modal').modal('show');
                    }
                })
                .catch(function(err){
                    console.log(err)
                    $('#fetching-data-modal').modal('hide');
                });
        }
    }

    /**********************************************************************
     * Page Events
    **********************************************************************/
    

    $('#id_activity').on('change', function(){
        selectActivity = $('#id_activity').val() ? $('#id_activity').find(':selected').text() : null;

        if(selectActivity){
            if(selectActivity == 'BTS Rehoming'){
                $("#stb-input-fields").addClass('d-none');
                $(".input-grp-container").addClass('d-none');
                $("#rehoming-input-fields").removeClass('d-none');
                
                $("#save-activity").prop("disabled", false);
                $("#id_siteid").prop('required', false)
                $("#id_tech").prop('required', false)
                $("#id_band").prop('required', false)
                
                $("#to_bsc_rnc").prop('required', true);
                $("#multiselect_to").prop('required', true);
            }else{
                $("#stb-input-fields").removeClass('d-none');
                $(".input-grp-container").removeClass('d-none');
                $("#rehoming-input-fields").addClass('d-none');

                $('select.select2').prop("disabled", false);
                $("#save-activity").prop("disabled", false);
                $("#id_siteid").prop('required', true);
                $("#id_tech").prop('required', true);
                $("#id_band").prop('required', true);

                $("#to_bsc_rnc").prop('required', false);
                $("#multiselect_to").prop('required', false);
                render_view();
            }
        }
    });

    $('#id_siteid').on('change', function(){
        selectSiteid = $('#id_siteid').val() ? $('#id_siteid').find(':selected').text() : null;
        $('#id_tech').val(null).trigger('change');
    });

    $('#id_tech').on('change', function(){
        selectTech = $('#id_tech').val() ? $('#id_tech').find(':selected').text() : null;
        $('#id_band').val(null).trigger('change');
    });

    $('#id_band').on('change', function(){
        selectBand = $('#id_band').val() ? $('#id_band').find(':selected').text() : null;
        render_view();
    });

    $('#filtered-device-table tbody').on('click', 'tr td button.dt-row-discard', function(e){
        e.preventDefault();
        MyDataTableActions.set_info(selectActivity, selectSiteid, selectTech, selectBand)
        MyDataTableActions.discard_table_row('#filtered-device-table', this, G_DISCARDED_NE_DATA);
        update_form_fields();
    });

    $('#filtered-cell-table tbody').on('click', 'tr td button.dt-row-discard', function(e){
        e.preventDefault();
        MyDataTableActions.set_info(selectActivity, selectSiteid, selectTech, selectBand)
        MyDataTableActions.discard_table_row('#filtered-cell-table', this, G_DISCARDED_NE_DATA);
        update_form_fields();
    });

    $('#filtered-trx-table tbody').on('click', 'tr td button.dt-row-discard', function(e){
        e.preventDefault();
        MyDataTableActions.set_info(selectActivity, selectSiteid, selectTech, selectBand)
        MyDataTableActions.discard_table_row('#filtered-trx-table', this, G_DISCARDED_NE_DATA);
        update_form_fields();
    });

    $('#from_bsc_rnc').on('change', function(){
        device = $('#from_bsc_rnc').val() ? $('#from_bsc_rnc').find(':selected').text() : null;
        get_bscrnc_nes(device).then(function(data){
            two_sides_multiselect_left = $('#multiselect');
            two_sides_multiselect_right = $('#multiselect_to');
            two_sides_multiselect_right.html('');
            if(data['count'] > 0){
                two_sides_multiselect_left.html('');
                for(i in data['results']){
                    item = data['results'][i];
                    two_sides_multiselect_left.append(`<option value="${item['site']}_${item['band']}_${item['tech']}">${item['site']}_${item['band']}_${item['tech']}</option>`);
                }
            }
        }).catch(e => console.log(e));
    });

    $('#missing-data-modal').on('hidden.bs.modal', function(){
        $('#missing-data-msg').html('');
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

    $('#from_bsc_rnc').select2({
        placeholder: 'Select BSC/RNC',
        ajax: {
            url: "/edrar/data/select2/bscrnc/",
            dataType: 'json',
        }
    });

    $('#to_bsc_rnc').select2({
        placeholder: 'Select BSC/RNC',
        ajax: {
            url: "/edrar/data/select2/bscrnc/",
            dataType: 'json',
        }
    });

    
    // function set_activity_select(activity){
    //     let activity_selected = false;
    //     $('#id_activity option').filter(function(){
    //         if( $(this).text() == activity){
    //             $(this).prop('selected', true).trigger("change");
    //             activity_selected = true;
    //         }
    //     });

    //     if(activity_selected){
    //         $('select.select2').prop("disabled", false);
    //         $("#save-activity").prop("disabled", false);
    //         render_view();
    //     }
    // }

    // function set_site_id_select(siteid){
    //     $('#id_activity option').filter(function(){
    //         if( $(this).text() == siteid){
    //             $(this).prop('selected', true).trigger("change");
    //         }
    //     });
    // }

    // function set_tech_select(tech){
    //     $('#id_activity option').filter(function(){
    //         if( $(this).text() == tech){
    //             $(this).prop('selected', true).trigger("change");
    //         }
    //     });
    // }

    // function set_band_select(band){
    //     $('#id_activity option').filter(function(){
    //         if( $(this).text() == band){
    //             $(this).prop('selected', true).trigger("change");
    //         }
    //     });
    // }


    disable_stb_select_fields();
    clear_tables();
    hide_text_field_containers();
    hide_general_input_container();

    $('#multiselect').multiselect();

    if(url_params.hasOwnProperty('edit')){
        url = `/edrar/data/activity/${url_params['activity']}/?edit=${url_params['edit']}`;
        get_activity_data(url).then(function(data){
            activity_id = data.activity;
            if(url_params['edit']){
                //Setting activity_id to 7 = Correction, for edit action.
                activity_id = 7;
            }
            $('#id_activity').val(activity_id).trigger('change');
            $('#id_siteid').val(data.siteid).trigger('change');
            $('#id_tech').val(data.tech).trigger('change');
            $('#id_band').val(data.band).trigger('change');
            G_LOGGED_ACTIVITY = data;
        }).catch(e => console.log(e));
    }
});