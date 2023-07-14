$(document).ready(function() {
    $('#periodo').change(function() {
        // Vaciamos el select de años
        $('#año').empty();

        // Obtenemos el valor del periodo seleccionado y eliminamos los paréntesis y los espacios
        var periodo = $(this).val().replace(/\s/g, '').replace(/[\(\)]/g, '').split(',');

        // Recorremos desde el año de inicio hasta el año final
        for (var i = parseInt(periodo[0]); i <= parseInt(periodo[1]); i++) {
            // Añadimos cada año como una opción en el select de años
            $('#año').append('<option value="' + i + '">' + i + '</option>');
        }
    }).change(); // Disparamos el evento change
});
