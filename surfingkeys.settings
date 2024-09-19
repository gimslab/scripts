settings.blacklistPattern=/^https?:\/\/(keep.google.com|calendar.google.com|colab.research.google.com|mail.google.com|docs.google.com|www.lucidchart.com|co...ng.*\.sharepoint\.com|metric.co...ng.net|app\.smartsheet\.com)/i;

api.unmapAllExcept(['S','x','f','E','R'], /\/bts.co...ng.net\//i);

api.unmap('e',/^https?:\/\/wiki.gimslab.com/i);
api.unmap('e',/^https?:\/\/h.gimslab.com/i);

var wikiCpNet=/^https?:\/\/wiki.co...ng.net/i;
api.unmap('?',wikiCpNet);
api.unmap('[',wikiCpNet);
api.unmap('e',wikiCpNet);
api.unmap('l',wikiCpNet); // label
api.unmap('c',wikiCpNet); // create

var youtubeCom=/^https?:\/\/youtube.com/i;
api.unmap('?',youtubeCom);
api.unmap('<',youtubeCom);
api.unmap('>',youtubeCom);
api.unmap('i',youtubeCom);

var githubCom=/^https?:\/\/github.com/i;
api.unmap('?',githubCom);

api.unmapAllExcept(['f','i','O','su','yt'], /^https?:\/\/outlook.office.com/i);

var gerrit=/^https?:\/\/gerrit.co...ng.net/i;
api.unmap('?', gerrit);
api.unmap('c', gerrit);

api.iunmap(":"); // disable emoji
// Hints.characters = 'acdfghijklmnopqrsuvwx'; // default is 'asdfgqwertzxcvb'

api.addSearchAlias('s', 'stackoverflow', 'http://stackoverflow.com/search?q='); // ss to search stackoverflow

api.aceVimMap(',,', '<Esc>', 'insert');

api.mapkey('<Ctrl-y>', 'Show me the money', function() {
    api.Front.showPopup('HI~');
});

var arr=[117,112,97];
var cp="";for(var i in arr) cp += String.fromCharCode(arr[i]);

api.mapkey('sj', 'open jira(BTS) in a new tab', function(){
    api.Front.showEditor('', function(data) {
        if(data)
            api.tabOpenLink('https://bts.co'+cp+'ng.net/browse/SADP-'+((data+"").replace(/[^0-9]/g,"")) );
        else
            api.tabOpenLink('https://bts.co'+cp+'ng.net/');
    }, 'url');
});

// override default
api.mapkey('sw', 'open wiki.cp in a new tab', function(){
    api.Front.showEditor('', function(data) {
        if(data)
            api.tabOpenLink('https://wiki.co'+cp+'ng.net/dosearchsite.action?cql=siteSearch+~+%22'+data+'%22+and+space.type+%3D+%22favourite%22&queryString='+data);
        else
            api.tabOpenLink('https://wiki.co'+cp+'ng.net/dosearchsite.action?queryString=&where=conf_favorites&type=&lastModified=&contributor=&contributorUsername=');
    }, 'url');
});

api.mapkey('sr', 'open recon.cp in a new tab', function(){
    api.Front.showEditor('', function(data) {
        if(data)
            api.tabOpenLink('https://finance.co'+cp+'ng.net/goods/recon?orderId='+data);
        else
            api.tabOpenLink('https://finance.co'+cp+'ng.net/goods/recon?orderId=00000');
    }, 'url');
});


