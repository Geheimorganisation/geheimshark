var Selfshark = (function (jQuery) {
	"use strict";
	var $ = jQuery.sub();

	function selfshark() {
		var next,
			shark = this,
			player = $("#player");

		// sortable playlist
		$("#playlist").sortable();

		// player event handlers
		player.bind('ended', function() {
			// check if there is a next song
			next = $("ul#playlist #pl_" + player.data("id")).next();
			if(next) {
				// get+play it
				$.getJSON('/api/get/id?id=' + next.attr("id").replace("pl_", ""), function(val) {
					shark.play(val["file"]);
				});
			}
		});
	}

	(function (fn) {
		fn.search = function () {
			// get the search value
			var val  = $("#searchq").val(),
				list = $("#songlist");
			
			// search
			$.getJSON('/api/get/search?q=' + val, function(data) {
				// clear the list
				list.empty();
				// set new items
				$.each(data, function(key, val) {
					list.append("<li id=\"sq_" + val["id"] + "\"><a href=\"javascript:selfshark.addToPlaylist('" + val["id"] + "');\">" + val["artist"] + " — " + val["title"] + "</a></li>");
				});
			});
		};
		fn.addToPlaylist = function (id) {
			var list = $("#playlist");

			// get the songs data
			$.getJSON('/api/get/id?id=' + id, function(val) {
				list.append("<li id=\"pl_" + val["id"] + "\"><a href=\"javascript:selfshark.play('" + val["file"] + "');\">" + val["artist"] + " — " + val["title"] + "</a></li>");
			});
		};
		fn.removeFromPlaylist = function(id) {
			$("#pl_" + id).remove();
		};
		fn.clearPlaylist = function () {
			$("#playlist").empty();
		};
		fn.play = function (path) {
			var player = $("#player").get(0);
			player.src = path;
			$("#player").data("id", $.sha1(path));
			player.play();
		};
	}(selfshark.prototype));

	return selfshark;
}(jQuery));