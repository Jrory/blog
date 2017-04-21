/**
 * Created by yujian on 17/4/17.
 */
var editor;
$(function(){
    KindEditor.ready(function(K) {
              editor = K.create('#comment', {
                  afterBlur: function () { this.sync();},
                  height:'200px',
                  uploadJson: '/admin/upload/kindeditor',
              });
        });
})





