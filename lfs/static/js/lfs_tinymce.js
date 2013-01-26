var editor;

function addEditor(selector, hide_save, height) {
    if (hide_save == true) {
        buttons = "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,bullist,numlist,|,forecolor,backcolor,styleselect,formatselect,imagebrowser,image,media,|,link,mylink,unlink,|,removeformat,code,|,fullscreen"
    }
    else {
        buttons  = "save,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,bullist,numlist,|,forecolor,backcolor,styleselect,formatselect,imagebrowser,image,media,|,link,mylink,unlink,|,removeformat,code,|,fullscreen"
    }

    if (!height) {
        height = "480";
    }

    // Theme options
    $(selector).tinymce({
        // Location of TinyMCE script
        script_url : STATIC_URL + 'tiny_mce-3.5.8/tiny_mce.js',

        // General options
        theme : "advanced",
        plugins : "advimage,safari,save,iespell,directionality,fullscreen,xhtmlxtras,media",

        theme_advanced_buttons1 : buttons,
        theme_advanced_buttons2 : "",
        theme_advanced_buttons3 : "",
        theme_advanced_buttons4 : "",
        theme_advanced_toolbar_location : "top",
        theme_advanced_toolbar_align : "left",
        save_onsavecallback : "save",
        relative_urls : false,
        verify_html : false,
        height : height,
        content_css : STATIC_URL + "css/tinymce_styles.css",
        setup : function(ed) {
            ed.addButton('imagebrowser', {
                // TODO: use gettext
                title : 'Image browser',
                image : STATIC_URL + 'icons/tinymce_imagebrowser_icon.gif',
                onclick : function(e) {
                    imagebrowser(e, ed);
                }
            });
        }
   });
}


var TINYMCE_FIELD_IDS = [{id: "#id_description", hide_save: false, height: null},
                         {id: "#id_short_description", hide_save: false, height: '200'},
                         {id: "#id_short_text", hide_save: false, height: '200'},
                         {id: "#id_body", hide_save: false, height: null},
                         {id: "#id_html", hide_save: false, height: null},
                         {id: "#id_note", hide_save: false, height: '100'}];

function update_editor() {
    /* for each field first detach tinymce and then attach again */
    $.each(TINYMCE_FIELD_IDS, function(idx, item){
        // translated fields
        $.each(TRANSLATION_LANGUAGES, function(idx2, lang){
            if (typeof(tinyMCE) != 'undefined'){
                $(item['id'] + "_" + lang).tinymce().remove();
            }
            addEditor(item['id'] + "_" + lang, item['hide_save'], item['height']);
        });

        // not translated fields
        $.each(TINYMCE_FIELD_IDS, function(idx, item){
            if (typeof(tinyMCE) != 'undefined'){
                $(item['id']).tinymce().remove();
            }
        });
        addEditor(item['id'], item['hide_save'], item['height']);
    });
}


function save(ed) {
    $("#" + ed.id).parents("form:first").ajaxSubmit({
        dataType: "json",
        success : function(data) {
            show_message(data["message"]);
        }
    })
}

function imagebrowser(e, ed) {
    editor = ed;
    node = editor.selection.getNode();
    url = node.src || "";
    title = node.title || "";
    klass = node.className || ""
    var id = $("#obj-id").attr("data");
    $.get(LFS_MANAGE_IMAGEBROWSER_URL + "?url=" + url + "&title=" + title + "&class=" + klass, function(data) {
        data = $.parseJSON(data);
        $("#dialog").html(data["html"]);
    });

    $("#dialog").dialog({
        autoOpen: false,
        closeOnEscape: true,
        modal: true,
        width: 800,
        height: 500,
        draggable: false,
        resizable: false,
        position: ["center", "center"]
    });

    $("#dialog").dialog("open");
}

function insertHTML(html) {
    editor.selection.setContent(html);
}
