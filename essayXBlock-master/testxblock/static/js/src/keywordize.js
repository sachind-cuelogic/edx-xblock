/**
* @author Zack Perdue / Ziggidy Creative
*
* http://zackperdue.com
* http://ziggidycreative.com
*
* Version 1.0
* Copyright (c) 2014 Zack Perdue
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/mit-license.php
*/

(function($){
 
  $.fn.keywordize = function(config, callback)
  {

    var options = {
      dictionary: [],
      expression: function(entry){ 

        return new RegExp("("+entry.keyword+")", 'ig');
      },
      template: function(entry){ 
        return '<a href="#" class="tooltip" title="'+entry.definition+'">$1</a>';
      }
    }

    $.extend(options, config, true);

    return this.each(function(){

      var
        scope       = $(this),
        text        = scope.html()
      ;

      $(options.dictionary).each(function(){

        var entry = this;

        text = text.replace(
          options.expression(entry),
          options.template(entry)
        );

      });

      scope.html(text);

      if (typeof callback === 'function')
        callback.call();

    });
  };

}(jQuery));