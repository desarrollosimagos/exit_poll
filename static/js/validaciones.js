$(document).ready(function() {
    $("input:text,select,textarea,input:password").attr('class','form-control');
    
//    $('#josue').DataTable( {
//	responsive: true
//    } );
//$("input:submit,button,input:file").attr('class','btn btn-success');



////////////////////////////////////////////////////////////////////////////////////////////////////////
// Limpiar Campos
////////////////////////////////////////////////////////////////////////////////////////////////////////

	    $('#limpiar').click(function(){
		$('select').select2('val',0)
		$('input[type="text"],textarea').val('')
		$('#id_cod_municipio,#id_cod_sector,#id_cod_parroquia,#id_circuito,#id_cod_pol, #id_cod_n').find('option:gt(0)').remove().end();		
	    });

////////////////////////////////////////////////////////////////////////////////////////////////////////
// Al cambiar de opción en el combo de municipio dependientes de los estados
////////////////////////////////////////////////////////////////////////////////////////////////////////
    $('#id_cod_estado').change(function() {
	var id_est = $('#id_cod_estado').val();
    $('#id_circuito,#id_cod_municipio,#id_cod_parroquia').find('option:gt(0)').remove().end().select2('val', '0');
    
	if (id_est > 0) {
	    $.get('/configuraciones/topologia/parroquias/busqueda_ajax/', {'id':id_est}, function(data) {
		var option = "";
		$.each(data, function(i) {
		    option += "<option value=" + data[i].pk + ">" + data[i].fields.municipio + "</option>";
		});
		$('#id_cod_municipio').append(option);
	    }, 'json');
	$.get('/configuraciones/topologia/municipios/circuito_ajax/', {'id':id_est}, function(data) {
	    var option = "";
	    $.each(data, function(i) {
		option += "<option value=" + data[i].pk+ ">" + data[i].fields.n_circuito + "</option>";
		});
		$('#id_circuito').append(option);
	    }, 'json');
	}
    });

////////////////////////////////////////////////////////////////////////////////////////////////////////
// Al cambiar de option en el combo parroquia dependientes de los municipios
////////////////////////////////////////////////////////////////////////////////////////////////////////
    $('#id_cod_municipio').change(function() {
	var id_est  = $('#id_cod_estado').val();
	var id_mun  = $("#id_cod_municipio").val();
	var id_parr = $('#id_cod_parroquia').val();
	
    $('#id_cod_parroquia').find('option:gt(0)').remove().end().select2('val', '0');
	if (id_est > 0 && id_mun > 0) {
	
	    $.get('/configuraciones/topologia/parroquias/busqueda_ajax2/', {'id_est':id_est,'id_mun':id_mun}, function(data) {
		var option = "";
		$.each(data, function(i) {
		    option += "<option value=" + data[i].pk + ">" + data[i].fields.parroquia + "</option>";
		});
		$('#id_cod_parroquia').append(option);
	    }, 'json');
	}
    });


////////////////////////////////////////////////////////////////////////////////////////////////////////
// Al cambiar de option en el combo municipios dependientes de los circuitos
////////////////////////////////////////////////////////////////////////////////////////////////////////
    $('#id_circuito').change(function() {
        var id_est  = $('#id_cod_estado').val();
        var id_cir  = $("#id_circuito").val();
        var id_mun  = $("#id_cod_municipio").val();
        
        if (id_est > 0 && id_cir > 0) {
            $('#id_cod_municipio').find('option:gt(0)').remove().end().select2('val', '0');
            $.get('/configuraciones/topologia/municipios/ajax_cir_mun/', {'id_est':id_est,'id_cir':id_cir}, function(data) {
           
            var option = "";
            $.each(data, function(i) {
                option += "<option value=" + data[i].pk + ">" + data[i].fields.municipio + "</option>";
                
            });
            $('#id_cod_municipio').append(option);
            }, 'json');
        }
    });


    
    
////////////////////////////////////////////////////////////////////////////////////////////////////////
// Al cambiar de option en el combo sector dependientes de las Parroquias
////////////////////////////////////////////////////////////////////////////////////////////////////////
    $('#id_cod_parroquia').change(function() {
	var id_est  = $('#id_cod_estado').val();
	var id_mun  = $("#id_cod_municipio").val();	
	var id_parr = $('#id_cod_parroquia').val();
	var id_sec  = $("#id_cod_sector").val();
	
	$('#id_cod_sector').select2('val', '0');
	if (id_est > 0 && id_mun > 0) {	
	    $.get('/configuraciones/topologia/poligonales/busqueda_sector/', {'id_est':id_est,'id_mun':id_mun,'id_parr':id_parr}, function(data) {
	    var option = "";
		$.each(data, function(i) {
		    option += "<option value=" + data[i].pk + ">" + data[i].fields.sector + "</option>";
		});
		$('#id_cod_sector').append(option);
	    
	    }, 'json');
	}
    
    });


////////////////////////////////////////////////////////////////////////////////////////////////////////
// Al cambiar de option en el combo poligonales dependientes de los sectores
////////////////////////////////////////////////////////////////////////////////////////////////////////
    $('#id_cod_sector').change(function() {
    var id_est  = $('#id_cod_estado').val();
    var id_mun  = $("#id_cod_municipio").val();	
    var id_parr = $('#id_cod_parroquia').val();
    var id_sec  = $("#id_cod_sector").val();
    var id_pol  = $("#id_cod_pol").val();
    
    $('#id_cod_pol').select2('val', '0');
    if (id_est > 0 && id_mun > 0 && id_parr > 0) {	
    $.get('/configuraciones/topologia/poligonales/busqueda_poligonal/', {'id_est':id_est,'id_mun':id_mun,'id_parr':id_parr,'id_sec':id_sec}, function(data) {
    var option = "";
    $.each(data, function(i) {
    option += "<option value=" + data[i].pk + ">" + data[i].fields.poligonal + "</option>";
    });
    $('#id_cod_pol').append(option);
    
    }, 'json');
    }
    
    });



////////////////////////////////////////////////////////////////////////////////////////////////////////
// Al cambiar de option en el combo centros dependientes de los sectores
////////////////////////////////////////////////////////////////////////////////////////////////////////
    $('#id_cod_parroquia').change(function() {
	var id_est  = $('#id_cod_estado').val();
	var id_mun  = $("#id_cod_municipio").val();	
	var id_parr = $('#id_cod_parroquia').val();
	var id_cen  = $("#id_cod_n").val();
	
	$('#id_cod_n').find('option:gt(0)').remove().end();
	if (id_est > 0 && id_mun > 0) {	
	    $.get('/configuraciones/centros/busqueda_centros/', {'id_est':id_est,'id_mun':id_mun,'id_parr':id_parr}, function(data) {
	    var option = "";
		$.each(data, function(i) {
		    option += "<option value=" + data[i].fields.cod_n + ">" + data[i].fields.nombre + "</option>";
		});
		$('#id_cod_n').append(option);
	    
	    }, 'json');
	}
    
    });
    
    
    
//    $('#id_cod_sector').change(function() {
//	var id_est  = $('#id_cod_estado').val();
//	var id_mun  = $("#id_cod_municipio").val();	
//	var id_parr = $('#id_cod_parroquia').val();
//	var id_sec  = $("#id_cod_sector").val();
//	var id_cen  = $("#id_cod_n").val();
//    
//    $('#id_cod_n').find('option:gt(0)').remove().end();
//    if (id_est > 0 && id_mun > 0 && id_parr > 0) {	
//	    $.get('/configuraciones/topologia//busqueda_centro/', {'id_est':id_est,'id_mun':id_mun,'id_parr':id_parr,'id_sec':id_sec}, function(data) {
//		var option = "";
//		$.each(data, function(i) {
//		    option += "<option value=" + data[i].fields.cod_n + ">" + data[i].fields.nombre + "</option>";
//		});
//		$('#id_cod_n').append(option);
//	    
//	    }, 'json');
//	}
//    
//    });

////////////////////////////////////////////////////////////////////////////////////////////////////////
// Al cambiar de opción en el combo de Categoria
////////////////////////////////////////////////////////////////////////////////////////////////////////
    $('#id_categoria_eleccion').change(function() {
	var id_cate = $('#id_categoria_eleccion').val();
	$('#id_tipo_eleccion').select2('val', '0');
	$('#id_eleccion').select2('val', '0');
	if (id_cate > 0) {
	    $.get('/elecciones/tipo_ajax/', {'id':id_cate}, function(data) {
		var option = "";
		$.each(data, function(i) {
		
		    option += "<option value=" + data[i].pk+ ">" + data[i].fields.tipo + "</option>";
		});
		$('#id_tipo_eleccion').append(option);
	    }, 'json');
	}
    
    });
    
////////////////////////////////////////////////////////////////////////////////////////////////////////
// Cambiar candidatos en base a la eleccion
////////////////////////////////////////////////////////////////////////////////////////////////////////
    $('#id_eleccion').change(function() {
	var id_ele = $('#id_eleccion').val();
	$('#id_candidato').find('option:gt(0)').remove().end();
	if (id_ele > 0) {
	    $.get('/reportes/graficas_candidatos/eleccion_candidato/', {'id':id_ele}, function(data) {
		var option = "";
		$.each(data, function(i,obj) {
		    option += "<option value=" + obj.id+ ">" + obj.nombre +" "+obj.apellido + "</option>";
                });
		$('#id_candidato').append(option);
	    }, 'json');
	}
    
    });
////////////////////////////////////////////////////////////////////////////////////////////////////////
// Al cambiar de opción en el combo de Estado monte los circuitos
////////////////////////////////////////////////////////////////////////////////////////////////////////
    $('#id_cir_estado').change(function() { 
    var id_est = $('#id_cir_estado').val();
	$('#id_circuito').find('option:gt(0)').remove().end();
	if (id_est > 0) {
	    $.get('/configuraciones/topologia/municipios/circuito_ajax/', {'id':id_est}, function(data) {
		var option = "";
		$.each(data, function(i) {
		    option += "<option value=" + data[i].pk+ ">" + data[i].fields.n_circuito + "</option>";
		});
		$('#id_circuito').append(option);
	    }, 'json');
	}
    });


////////////////////////////////////////////////////////////////////////////////////////////////////////
// Al sleccionar un checkbo
////////////////////////////////////////////////////////////////////////////////////////////////////////
//$("input:checkbox[name='niveles']").change(function() {
//    var este = $(this)
//    if ($(this).is(':checked')) {
//        $("input:checkbox[name='niveles']").not(este).prop('disabled',true)
//    } else {
//        $("input:checkbox[name='niveles']").not(este).prop('disabled',false)
//    }
//});

////////////////////////////////////////////////////////////////////////////////////////////////////////
// Carga el codigo del centro
////////////////////////////////////////////////////////////////////////////////////////////////////////
    $('#id_cod_estado').change(function(){
	var e = $('#id_cod_estado').val();
	$('#id_cod_n').val(e);
    });

    $('#id_cod_municipio').change(function(){
	var e = $('#id_cod_estado').val();
	var m = $('#id_cod_municipio').val();
	if (m.length == 1){
	    a = "0"+m
	}
	else{
	    a = m
	}
	$('#id_cod_n').val(e+''+a);
    });


    $('#id_cod_parroquia').change(function(){
	var e = $('#id_cod_estado').val();
	var m = $('#id_cod_municipio').val();
	var p = $('#id_cod_parroquia').val();
	
	if (m.length == 1){
	    a = "0"+m
	}
	else{
	    a = m
	}
	if (p.length == 1){
	    o = "0"+p
	}
	else{
	    o = p
	}
	$('#id_cod_n').val(e+''+a+''+o);
    });
});


////////////////////////////////////////////////////////////////////////////////////////////////////////
// Funcion para Cargar foto 
////////////////////////////////////////////////////////////////////////////////////////////////////////

function PreviewImage() {
        var oFReader = new FileReader();
        oFReader.readAsDataURL(document.getElementById("id_foto").files[0]);

        oFReader.onload = function (oFREvent) {
            document.getElementById("uploadPreview").src = oFREvent.target.result;
        };
    }

////////////////////////////////////////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////////////////////////////////////////
// Funcion global para depurar
////////////////////////////////////////////////////////////////////////////////////////////////////////
function eliminar_data(pk_id, url) {
    id_data= String(pk_id)
    r = confirm("¿Realmente desea eliminar el registro?!");
    if (r == true) {
        location.href=url+id_data;
    }
};
////////////////////////////////////////////////////////////////////////////////////////////////////////
