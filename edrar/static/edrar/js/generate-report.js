
$(document).ready(function() {
    var DAILY_ACTIVITY_REPORT_DT = Object.create(dt);

    async function export_activity_data_from_edrar(report_param){
        const response = await fetch(`/edrar/report/export/`, {
            method: 'POST',
            cache: 'no-cache',
            headers: {
                "X-CSRFToken": report_param['csrfmiddlewaretoken'],
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(report_param)
        });

        return response.json();
    }

    function get_generate_report_filter(){
        activityData = {}
        $('#activity-data-filter-form *').filter(':input').each(function(){
            let propertyName = $(this).attr('name');
            if(propertyName == 'activity'){
                activityData[propertyName] = $(`#id_${propertyName}`).select2('data');
            }else if(propertyName){
                activityData[propertyName] = $(this).val();
            }
        });
        console.log(activityData);
        return activityData;
    }

    function set_da_report_dt_options(data){
        var options = {
            'data': data.daily_activities,
            'columns': [
                {data: 'date_logged'},
                {data: 'activity'},
                {data: 'siteid'},
                {data: 'site_name'},
                {data: 'band'},
                {data: 'tech'},
                {data: 'vendor'},
                {data: 'homing'},
                {data: 'device_name'},
                {data: 'bts_id'},
                {data: 'cell_id'},
                {data: 'cell_name'},
                {data: 'sac'},
                {data: 'lac'},
                {data: 'city'},
                {data: 'province'},
                {data: 'region'},
                {data: 'area'},
                {data: 'aor'},
                {data: 'remarks'},
            ],
            'columnDefs': [
                {name: 'date_logged', searchable: true, visible: true, targets: [0]},
                {name: 'activity', searchable: true, visible: true, targets: [1]},
                {name: 'siteid', searchable: true, visible: true, targets: [2]},
                {name: 'site_name', searchable: true, visible: true, targets: [3]},
                {name: 'band', searchable: true, visible: true, targets: [4]},
                {name: 'tech', searchable: true, visible: true, targets: [5]},
                {name: 'vendor', searchable: true, visible: true,  targets: [6]},
                {name: 'homing', searchable: true, visible: false, targets: [7]},
                {name: 'device_name', searchable: true, visible: false,  targets: [8]},
                {name: 'bts_id', searchable: false, visible: false, targets: [9]},
                {name: 'cell_id', searchable: false, visible: false, targets: [10]},
                {name: 'cell_name', searchable: false, visible: false, targets: [11]},
                {name: 'sac', searchable: false, visible: false, targets: [12]},
                {name: 'lac', searchable: false, visible: false, targets: [13]},
                {name: 'city', searchable: true, visible: true, targets: [14]},
                {name: 'province', searchable: true, visible: true, targets: [15]},
                {name: 'region', searchable: true, visible: true, targets: [16]},
                {name: 'area', searchable: true, visible: true, targets: [17]},
                {name: 'aor', searchable: true, visible: true, targets: [18]},
                {name: 'remarks', searchable: true, visible: true, targets: [19]},
            ],
        }
        return options;
    }

    $('#id_activity').select2({
        multiple: true,
        allowClear: true,
        placeholder: 'Select Activities',
        ajax: {
            url: "/edrar/data/select2/activity-autocomplete/",
            dataType: 'json',
        }
    });

    $('#id_activity').on('select2:clear', function(e) {
        $('#download-report').addClass('btn-secondary disabled').removeClass('btn-warning');
        $('#download-report').attr('href', `#`);
        $('#activity-datatable').addClass('d-none');
        dt.clear_table('#activity-datatable');
        $('#generate-report').html('Generate Report');
        $('#id_project_name').val('');
        $('#id_start').val('');
        $('#id_end').val('');
    });

    function is_valid(report_filter_params){
        for([key, val] in Object.values(report_filter_params)){
            if(key == 'start' || key == 'end' && !val){
                return false;
            }else if(key == 'activity' && !val){
                return false;
            }
        }
        return true;
    }

    $("#generate-report").click(function(e){
        e.preventDefault();
        report_param = get_generate_report_filter();
        if(is_valid(report_param)){
            $('#download-report').addClass('btn-secondary disabled').removeClass('btn-warning');
            $('#download-report').attr('href', `#`);
            $('#activity-datatable').addClass('d-none');
            dt.clear_table('#activity-datatable');
            $('#activity-datatable-container > #data-failed-notif').remove();
            loading_button_html = `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading`;
            $('#generate-report').html(loading_button_html);
            dt.post_server_data('/edrar/report/', report_param, report_param['csrfmiddlewaretoken'])
                .then(function(data){
                    if(data.success){
                        $('#activity-datatable').removeClass('d-none');
                        $('#download-report').addClass('btn-warning').removeClass('btn-secondary disabled');
                        $('#download-report').attr('href', `/media/edrar/reports/${data.report_file}`);
                        dt_options = set_da_report_dt_options(data);
                        DAILY_ACTIVITY_REPORT_DT.table_options(dt_options);
                        DAILY_ACTIVITY_REPORT_DT.draw_table('#activity-datatable');
                        // url_param = new URLSearchParams(report_param).toString();
                        // console.log(url_param)
                        $('#generate-report').html('Generate Report');
                    }else{
                        failed_notif_html = `<div id="data-failed-notif" class="alert alert-warning alert-dismissible" role="alert">
                            <strong>Report generation failed!</strong> Check filter parameter.
                            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>`;
                        $('#activity-datatable-container').prepend(failed_notif_html);
                        $('#generate-report').html('Generate Report');
                    }
                })
                .catch(function(e){
                    $('#generate-report').html('Generate Report');
                    console.log(e);
                });
        }
    });

    $("#id_start").datepicker();
    $("#id_end").datepicker();
});