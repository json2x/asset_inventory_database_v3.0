
var MyDataTable = {
    'activity': null,
    'site': null,
    'tech': null,
    'band': null,
    'is_ne_missing': false,
    'is_data_missing': false,
    'missing_data_msg': [],
    'ne_info': {},
    'table_src': {'DEVICE': null, 'CELL': null, 'TRX': null},
    'set_info': function(activity, site, tech, band){
        this.activity = activity;
        this.site = site;
        this.tech = tech;
        this.band = band;
        this.is_ne_missing = false;
        this.is_data_missing = false;
        this.missing_data_msg = [];
        this.ne_info = {'Device': 0, 'Cell': 0, 'Trx': 0};
    },
    'evaluate_ne_info': function(){
        if(!this.ne_info['Device'] && !this.ne_info['Cell'] && !this.ne_info['Trx']){
            this.is_ne_missing = true;
            this.missing_data_msg = [`Network element ${this.site}_${this.tech}_${this.band} not found in the data source`];
        }
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
    'draw_device_table': function(dataSrcObjArray){
        //dataArray = G_NMS_SRC_ACTIVITY['DEVICE'].indexOf(this.activity) > -1? dataSrcObjArray['nms']: dataSrcObjArray['aid'];
        src = G_NMS_SRC_ACTIVITY['DEVICE'].indexOf(this.activity) > -1? 'nms':'aid';
        dataArray = (src == 'nms')? dataSrcObjArray['nms']: dataSrcObjArray['aid'];
        var options = {
            data: dataArray,
            processing: true,
            //select: true,
            columns: [
                {data: 'ems_id'},
                {data: 'device_id'},
                {data: 'parent_device_id'},
                {data: 'ne_type'},
                {data: 'record_status'},
                {data: 'dn'},
                {data: 'site_id'},
                {data: 'subdomain'},
                {data: 'vendor_id'},
                {data: 'domain'},
                {data: 'model'},
                {data: 'id'},
                {data: 'rel_id'},
                {
                    data: null,
                    className: 'dt-row-option text-right',
                    orderable: false,
                    defaultContent: `<button class="btn btn-sm btn-light py-0 dt-row-discard text-primary" data-tbl="device" data-src="${src}">\
                        <i class="fa fa-times" aria-hidden="true"></i>\
                    </button>`,
                },
            ],
            columnDefs: [
                {name: 'ems_id', searchable: true, targets: [0]},
                {name: 'device_id', searchable: true, targets: [1]},
                {name: 'parent_device_id', searchable: true, targets: [2]},
                {name: 'ne_type', searchable: true, targets: [3]},
                {name: 'record_status', searchable: false, targets: [4]},
                {name: 'dn', searchable: false, visible: false,  targets: [5]},
                {name: 'site_id', searchable: false, visible: false, targets: [6]},
                {name: 'subdomain', searchable: false, visible: false, targets: [7]},
                {name: 'vendor_id', searchable: false, visible: false,  targets: [8]},
                {name: 'domain', searchable: false, visible: false, targets: [9]},
                {name: 'model', searchable: false, visible: false, targets: [10]},
                {name: 'id', searchable: false, visible: false, targets: [11]},
                {name: 'rel_id', searchable: false, visible: false, targets: [12]},
            ],
            order: [[2,'asc']],
            createdRow: function(row, data, dataindex){
                $(row).addClass(`${src}-data`);
            }
        }
        
        this.ne_info['Device'] = dataArray.length;
        if(dataArray.length <= 0){
            this.is_data_missing = true;
            this.missing_data_msg.push(`Device for site ${this.site}_${this.tech}_${this.band} is/are not in the data source`);
        }
        this.table_src['DEVICE'] = src;
        this.draw_table('#filtered-device-table', options);
    },
    'draw_cell_table': function(dataSrcObjArray){
        //dataArray = G_NMS_SRC_ACTIVITY['CELL'].indexOf(this.activity) > -1? dataSrcObjArray['nms']: dataSrcObjArray['aid'];
        src = G_NMS_SRC_ACTIVITY['CELL'].indexOf(this.activity) > -1? 'nms':'aid';
        dataArray = (src == 'nms')? dataSrcObjArray['nms']: dataSrcObjArray['aid'];
        var options = {
            data: dataArray,
            processing: true,
            //select: true,
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
                {data: 'rel_id'},
                {
                    data: null,
                    className: 'dt-row-option text-right',
                    orderable: false,
                    defaultContent: `<button class="btn btn-sm btn-light py-0 dt-row-discard text-primary" data-tbl="cell" data-src="${src}">\
                        <i class="fa fa-times" aria-hidden="true"></i>\
                    </button>`,
                },
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
                {name: 'rel_id', searchable: false, visible: false, targets: [16]},
            ],
            order: [[1,'asc']],
            createdRow: function(row, data, dataindex){
                $(row).addClass(`${src}-data`);
            }
        }

        this.ne_info['Cell'] = dataArray.length;
        if(dataArray.length <= 0){
            this.is_data_missing = true;
            this.missing_data_msg = [`Cell for site ${this.site}_${this.tech}_${this.band} is/are not in the data source`];
        }
        this.table_src['CELL'] = src;
        options = this.table_options(options);
        this.draw_table('#filtered-cell-table', options);
    },
    'draw_trx_table': function(dataSrcObjArray){
        src = G_NMS_SRC_ACTIVITY['TRX'].indexOf(this.activity) > -1? 'nms':'aid';
        dataArray = (src == 'nms')? dataSrcObjArray['nms']: dataSrcObjArray['aid'];
        var options = {
            data: dataArray,
            processing: true,
            //select: true,
            columns: [
                {data: 'ems_id'},
                {data: 'trx_name'},
                {data: 'parent_id'},
                {data: 'homing_bts'},
                {data: 'admin_state'},
                {data: 'record_status'},
                {data: 'id'},
                {data: 'rel_id'},
                {
                    data: null,
                    className: 'dt-row-option text-right',
                    orderable: false,
                    defaultContent: `<button class="btn btn-sm btn-light py-0 dt-row-discard text-primary" data-tbl="trx" data-src="${src}">\
                        <i class="fa fa-times" aria-hidden="true"></i>\
                    </button>`,
                },
            ],
            columnDefs: [
                {name: 'ems_id', searchable: true, visible: false, targets: [0]},
                {name: 'trx_name', searchable: true, targets: [1], render: 
                    function ( data, type, row ) {
                        if(data.length > 30){
                            return `${data.substr(0,24)}.....${data.substr(-20)}`;
                        }else{
                            return data;
                        }
                    }
                },
                {name: 'parent_id', searchable: true, targets: [2]},
                {name: 'homing_bts', searchable: true, targets: [3]},
                {name: 'admin_state', searchable: true, targets: [4]},
                {name: 'record_status', searchable: true, targets: [5]},
                {name: 'id', searchable: false, visible: false, targets: [6]},
                {name: 'rel_id', searchable: false, visible: false, targets: [7]},
            ],
            order: [[2,'asc']],
            createdRow: function(row, data, dataindex){
                $(row).addClass(`${src}-data`);
            }
        }
    
        this.ne_info['Trx'] = dataArray.length;
        if(dataArray.length <= 0 ){
            this.is_data_missing = true;
            this.missing_data_msg.push(`TRX for site ${this.site}_${this.tech}_${this.band} is/are not in the data source`);
        }
        this.table_src['TRX'] = src;
        this.draw_table('#filtered-trx-table', options);
    }
};


var MyDataTableActions = {
    activity: null,
    site: null,
    tech: null,
    band: null,
    data_src: null,
    tbl_src: null,
    discard_tree: {
        'DEVICE': ['cell', 'trx'],
        'CELL': ['trx'],
        'TRX': null
    },
    set_info: function(activity, site, tech, band){
        this.activity = activity;
        this.site = site;
        this.tech = tech;
        this.band = band;
    },
    discard_table_row: function(tableId, btnClicked, discardedDataContainer){
        let table = $(tableId).DataTable();
        let data_src = $(btnClicked).attr('data-src');
        let tbl_src = ($(btnClicked).attr('data-tbl')).toUpperCase();
        let tr = $(btnClicked).parent().parent();
        let data = table.row(tr).data();
        let discarded = this.render_toggle_discard_table_row(tr);
        if(discarded){
            discardedDataContainer[data_src][tbl_src].push(data);
        }else{
            for(let i in discardedDataContainer[data_src][tbl_src]){
                if(data.id == discardedDataContainer[data_src][tbl_src][i].id){
                    discardedDataContainer[data_src][tbl_src].splice(i, 1);
                    break;
                }
            }
        }
        this.data_src = data_src;
        this.tbl_src = tbl_src;
        this.discard_related_rows_from_other_table(data, discarded);
    },
    discard_related_rows_from_other_table: function(refRowData, parentState){
        var rel_id = refRowData.rel_id;
        for(i in this.discard_tree[this.tbl_src]){
            var ref_tbl = this.discard_tree[this.tbl_src][i];
            var tableId = `#filtered-${ref_tbl}-table`;
            var table = $(tableId).DataTable();
            var myInstance = this;
            table.rows().every(function(){
                var row_data = this.data();
                if(myInstance.validate_referenced_row(refRowData, row_data)){
                    let discarded = myInstance.render_toggle_discard_of_child_table_row(this.node(), parentState);
                    if(discarded){
                        G_DISCARDED_NE_DATA[myInstance.data_src][(ref_tbl).toUpperCase()].push(row_data);
                    }else{
                        for(let i in G_DISCARDED_NE_DATA[myInstance.data_src][(ref_tbl).toUpperCase()]){
                            if(row_data.id == G_DISCARDED_NE_DATA[myInstance.data_src][(ref_tbl).toUpperCase()][i].id){
                                G_DISCARDED_NE_DATA[myInstance.data_src][(ref_tbl).toUpperCase()].splice(i, 1);
                                break;
                            }
                        }
                    }
                }
            });
        }
    },
    validate_referenced_row: function(refRowData, currRowData){
        var matched = false;
        if(this.tbl_src == 'DEVICE' && refRowData.rel_id == currRowData.rel_id){
            matched = true;
        }else if(this.tbl_src == 'CELL' && refRowData.rel_id == currRowData.rel_id 
        && refRowData.ems_id == currRowData.ems_id && refRowData.cell_name == currRowData.parent_id){
            matched = true;
        }
    
        return matched;
    },
    render_toggle_discard_table_row: function(tr){
        let discarded = false;
        if($(tr).hasClass('discard')){
            $(tr).removeClass('discard');
        }else{
            discarded = true;
            $(tr).addClass('discard');
        }
        
        return discarded;
    },
    render_toggle_discard_of_child_table_row: function(tr, state){
        let discarded = false;
        if(state){
            discarded = true;
            if(!$(tr).hasClass('discard')){
                $(tr).addClass('discard');
            }
        }else{
            if($(tr).hasClass('discard')){
                $(tr).removeClass('discard');
            }
        }
        
        return state;
    },
    // discard_related_rows_from_other_table_v1(){
    //     var src = this.data_src;
    //     var discarded_parent_ids = G_DISCARDED_NE_DATA[src][this.tbl_src].map(data => data.id);
    //     var parent_tbl = (this.tbl_src).toLowerCase();
    //     for(i in this.discard_tree[this.tbl_src]){
    //         var ref_tbl = this.discard_tree[this.tbl_src][i];
    //         var tableId = `#filtered-${ref_tbl}-table`;
    //         var table = $(tableId).DataTable();
    //         var myInstance = this;
    //         table.rows().every(function(){
    //             var row_data = this.data();
    //             if(ref_tbl == 'cell'){
    //                 if(Array.isArray(row_data['device'])){
    //                     reference_data = Object.values(row_data['device']).map(child => child);
    //                 }else{
    //                     reference_data = row_data['device']
    //                 }
    //                 for(let i in reference_data){
    //                     if(discarded_parent_ids.indexOf(reference_data[i].id) > -1){
    //                         myInstance.render_toggle_discard_table_row(this.node());
    //                         G_DISCARDED_NE_DATA[src][(ref_tbl).toUpperCase()].push(row_data);
    //                     }
    //                 }
    //             }else if(ref_tbl == 'trx'){
    //                 reference_data = G_NE_DATA[src].map(cell => cell);
    //                 for(let i in reference_data){
    //                     cell_trxs_id = Object.values(reference_data[i]['trx']).map(trx => trx.id);
    //                     if(cell_trxs_id.indexOf(row_data.id) > -1){
    //                         if(discarded_parent_ids.indexOf(reference_data[i].id) > -1){
    //                             myInstance.render_toggle_discard_table_row(this.node());
    //                             G_DISCARDED_NE_DATA[src][(ref_tbl).toUpperCase()].push(row_data);
    //                         }
    //                     }
    //                 }
    //             }
    //         });
    //         parent_tbl = ref_tbl;
    //         discarded_parent_ids = G_DISCARDED_NE_DATA[this.data_src][(ref_tbl).toUpperCase()].map(data => data.id);
    //     }
    // },
}