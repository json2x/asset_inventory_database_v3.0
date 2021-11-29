
var dt = {
    data: null,
    table: null,
    options: null,
    fetch_server_data: false,
    get_server_data: async function(url){
        fetch_server_data = 'GET';
        const response = await fetch(url, {
            method: 'GET',
            cache: 'no-cache',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        //this.data = response.json();
        //return this;
        return response.json();
    },
    post_server_data: async function(url, data, csrftoken){
        fetch_server_data = 'POST';
        const response = await fetch(url, {
            method: 'POST',
            cache: 'no-cache',
            headers: {
                "X-CSRFToken": csrftoken,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        //this.data = response.json();
        //return this;
        return response.json();
    },
    table_options: function(options){
        this.options = options;
        this.data = options.data;
        return this;
    },
    clear_table: function(tableId){
        if($.fn.dataTable.isDataTable(tableId)){
            $(tableId).DataTable().clear().destroy();
        }
        return this;
    },
    draw_table: function(tableId){
        this.clear_table(tableId);
        this.table=$(tableId).DataTable(this.options);
        
        return this;
    },
}

String.prototype.toProperCase = function () {
    return this.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
};