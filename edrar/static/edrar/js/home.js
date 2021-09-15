var HOME_DT = {}

$(document).ready(function() {

    async function fetch_row_full_data(id){
        const response = await fetch(`/edrar/data/activity/${id}/`, {
            method: 'GET',
            cache: 'no-cache',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        return response.json();
    }

    function show_details(tr, row) {
        data = row.data();
        fetch_row_full_data(data.id).then(function(data){
            dom = '<div class="row">';
            for(let[key, val] of Object.entries(data)){
                if(val){
                    dom += `<div class="col-sm-3"><label class="dt-child" for="${key}">${key.replace('_', ' ').toProperCase()}:</label> ${val}</div>`;
                }
            }
            dom += '</div>';
            row.child(dom).show();
            tr.addClass('shown');
        }).catch(e => console.log(e));
        // dom = '<div class="row"><div class="col-sm-3"></div></div>';
    }

    HOME_DT = Object.create(dt);
    var options = {
        ajax: '/edrar/data/datatable/activity/',
        searching: true,
        processing: true,
        serverSide: true,
        columns: [
            {data: 'id'},
            {
                data: null,
                searchable: false,
                orderable: false,
                className: 'row-controls',
                defaultContent: '<i class="fas fa-plus px-1 details"></i><i class="fas fa-edit px-1 edit"></i>'
            },
            {data: 'date_logged', searchable: false},
            {data: 'activity'},
            {data: 'siteid'},
            {data: 'tech'},
            {data: 'band'},
            {data: 'vendor'},
            {data: 'site_status'},
            {data: 'user'},
        ],
        columnDefs: [
            {name: 'id', searchable: false, visible: false, targets: [0]},
        ],
        order: [[2,'desc']],
        language: {
            "processing": "Loading. Please wait..."
        },
        // createdRow: function(row, data, dataindex){
        //     $(row).addClass(`${src}-data`);
        // }
    }
    HOME_DT.table_options(options);
    HOME_DT.draw_table('#activity-datatable');
    // console.log(HOME_DT);

    $('#activity-datatable tbody').on('click', 'td.row-controls > i.details', function () {
        var tr = $(this).closest('tr');
        var row = HOME_DT.table.row( tr );
        var loading_gif = `<div class="row"><div class="col text-center"><img class="loading-ellipsis" src="/static/edrar/img/loading-ellipsis-50px.gif" alt="loading"></div></div>`;
        if (row.child.isShown()){
            // This row is already open - close it
            row.child.hide();
            tr.removeClass('shown');
            $(this).removeClass('fa-minus');
            $(this).addClass('fa-plus');
        }else{
            // Open this row
            $(this).removeClass('fa-plus');
            $(this).addClass('fa-minus');
            row.child(loading_gif).show();
            show_details(tr, row);
        }
        
    } );

    $('#activity-datatable tbody').on('click', 'td.row-controls > i.edit', function () {
        var tr = $(this).closest('tr');
        var row = HOME_DT.table.row( tr );
        var data = row.data();
        window.location.href = `/edrar/activity/log?daily_activity=${data.id}&activity=Correction`;
    } );


});