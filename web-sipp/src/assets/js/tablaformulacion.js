document.addEventListener('DOMContentLoaded', function() {
    var dataManager = new ej.data.DataManager({
        url: getDataUrl,
        adaptor: new ej.data.UrlAdaptor(),
        crossDomain: true
    });
    var query = new ej.data.Query().from('data');

    dataManager.executeQuery(query).then(function(e) {
        var data = e.result;
        console.log(e.result); // Verificar los datos en la consola del navegador
        console.log(e.result[0].spopro_id);
        // Crea una instancia de TreeGrid
        let grid = new ej.treegrid.TreeGrid({
            dataSource: data,
            childMapping: 'subproductos',
            idMapping: 'spopro_id',
            parentIdMapping: 'spospro_id',
            height: 400,
            treeColumnIndex: 1,
            detailTemplate: '#template',
            detailDataBound: function(e) {
                let childGrid = new ej.grids.Grid({
                    dataSource: e.data.subproductos,
                    columns: [
                        { field: 'spospro_id', headerText: 'ID SubProducto', textAlign: 'center', width: 120 },
                        { field: 'spospr_descripcion', headerText: 'Descripcion del SubProducto', width: 150 },
                    ],
                });
                childGrid.appendTo(e.childGrid.querySelector("#childGrid"));
            },
            columns: [
                { field: 'spopro_id', headerText: 'ID Producto', textAlign: 'Center', width: 90 },
                { field: 'spopro_descripcion', headerText: 'Descripcion del Producto', width: 220 },
            ],
        });

        grid.appendTo('#Grid');

    });
});
