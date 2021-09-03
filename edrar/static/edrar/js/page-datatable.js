
var MyDataTable = {
    'activity': null,
    'site': null,
    'tech': null,
    'band': null,
    'set_info': function(activity, site, tech, band){
        this.activity = activity;
        this.site = site;
        this.tech = tech;
        this.band = band;
    },
    'draw_table': function(tableId, dataTableOptions){
        this.clear_table(tableId);
        dataTable=$(tableId).DataTable(dataTableOptions);
        $(`${tableId}-container`).show();
        $(`${tableId}-separator`).show();
        tableCleared = false;
    },
    'clear_table': function(tableId){
        if($.fn.dataTable.isDataTable(tableId)){
            $(tableId).DataTable().clear().destroy();
            $(`${tableId}-container`).hide();
            $(`${tableId}-separator`).hide();
        }
    },
    'table_options': function(options){
        switch(this.tech){
            case G_TECH_LIST['2G']:
                break;
            case G_TECH_LIST['3G']:
                options['columns'][8]['data'] = 'rnc_cid';
                options['columns'][10]['data'] = 'sac_ci_eutra';
                options['columnDefs'][8]['name'] = 'rnc_cid';
                options['columnDefs'][10]['name'] = 'sac_ci_eutra';
                break;
            case G_TECH_LIST['FD-LTE']:
                break;
            case G_TECH_LIST['TD-LTE']:
                break;
            case G_TECH_LIST['5G']:
                break;
            default:
        }
    
        return options;
    },
    'draw_device_table': function(dataArray){
        var options = {
            data: dataArray,
            processing: true,
            select: true,
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
            order: [[2,'asc']],
            language: {
                processing: 'Loading. Please wait...'
            }
        }
        options = this.table_options(options);
        this.draw_table('#filtered-device-table', options);
    },
    'draw_cell_table': function(dataArray){
        var options = {
            data: dataArray,
            processing: true,
            select: true,
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
            order: [[1,'asc']],
            language: {
                processing: 'Loading. Please wait...'
            }
        }
        
        options = this.table_options(options);
        this.draw_table('#filtered-cell-table', options);
    },
    'draw_trx_table': function(dataArray){
        var options = {
            data: dataArray,
            processing: true,
            select: true,
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
            language: {
                processing: 'Loading. Please wait...'
            }
        }
    
        options = this.table_options(options);
        this.draw_table('#filtered-trx-table', options);
    }
}

////////// TO REMOVE //////////

function F_Draw_Datatable(tableId, dataTableOptions){
    F_Clear_Table(tableId);
    dataTable=$(tableId).DataTable(dataTableOptions);
    $(`${tableId}-container`).show();
    $(`${tableId}-separator`).show();
    tableCleared = false;
}

function F_Clear_Table(tableId){
    if($.fn.dataTable.isDataTable(tableId)){
        $(tableId).DataTable().clear().destroy();
        $(`${tableId}-container`).hide();
        $(`${tableId}-separator`).hide();
    }
}

function F_Table_Options(tech, options){
    switch(tech){
        case G_TECH_LIST['2G']:
            break;
        case G_TECH_LIST['3G']:
            options['columns'][8]['data'] = 'rnc_cid';
            options['columns'][10]['data'] = 'sac_ci_eutra';
            options['columnDefs'][8]['name'] = 'rnc_cid';
            options['columnDefs'][10]['name'] = 'sac_ci_eutra';
            break;
        case G_TECH_LIST['FD-LTE']:
            break;
        case G_TECH_LIST['TD-LTE']:
            break;
        case G_TECH_LIST['5G']:
            break;
        default:
    }

    return options;
}

function F_Draw_Device_Datatable(dataArray){
    var options = {
        data: dataArray,
        processing: true,
        select: true,
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
        order: [[2,'asc']],
        language: {
            processing: 'Loading. Please wait...'
        }
    }
    options = F_Revise_Table_Option(tech, options);
    F_Draw_Datatable('#filtered-device-table', options);
}

function F_Draw_Cell_Datatable(dataArray){
    var options = {
        data: dataArray,
        processing: true,
        select: true,
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
        order: [[1,'asc']],
        language: {
            processing: 'Loading. Please wait...'
        }
    }

    options = F_Revise_Table_Option(tech, options);
    F_Draw_Datatable('#filtered-cell-table', options);
}

function F_Draw_Trx_Datatable(dataArray){
    var options = {
        data: dataArray,
        processing: true,
        select: true,
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
        language: {
            processing: 'Loading. Please wait...'
        }
    }

    options = F_Revise_Table_Option(tech, options);
    F_Draw_Datatable('#filtered-trx-table', options);
}