// not work now 20240919, you can check symptoms like errors in dev console while pressing alt-s, 1.17.0
// settings.blacklistPattern=/^https?:\/\/(keep.google.com|calendar.google.com|colab.research.google.com|mail.google.com|docs.google.com|www.lucidchart.com|lucid.app|co...ng.*\.sharepoint\.com|metric.co...ng.net|app\.smartsheet\.com)/i;
// settings.blocklistPattern = /((calendar|mail).google|trello|duolingo|youtube|udemy).com/i
// settings.blocklistPattern = /((calendar|mail|keep)\.google|trello|duolingo)\.com/i

/////////////
// unmap
//api.unmapAllExcept(['S','x','f','E','R'], /\/bts.co...ng.net\//i);

api.unmap('a',/.*/i);

api.unmap('e',/^https?:\/\/wiki.gimslab.com/i);
api.unmap('e',/^https?:\/\/h.gimslab.com/i);


var wikiCpNet=/^https?:\/\/wiki.co...ng.net/i;
api.unmap('?',wikiCpNet);
api.unmap('[',wikiCpNet);
api.unmap('e',wikiCpNet);
api.unmap('l',wikiCpNet); // label
api.unmap('c',wikiCpNet); // create


//var youtubeCom=/^https?:\/\/(www\.)?youtube.com/i;
//api.unmap('?',youtubeCom);
//api.unmap('<',youtubeCom);
//api.unmap('>',youtubeCom);
//api.unmap('i',youtubeCom);
//
//
//var githubCom=/^https?:\/\/github.com/i;
//api.unmap('?',githubCom);
//
//
//api.unmapAllExcept(['f','i','O','su','yt'], /^https?:\/\/outlook.office.com/i);
//
//
//var gerrit=/^https?:\/\/gerrit.co...ng.net/i;
//api.unmap('?', gerrit);
//api.unmap('c', gerrit);






// set theme
settings.theme = `
.sk_theme {
    font-family: Input Sans Condensed, Charcoal, sans-serif;
    font-size: 10pt;
    background: #24272e;
    color: #abb2bf;
}
.sk_theme tbody {
    color: #fff;
}
.sk_theme input {
    color: #d0d0d0;
}
.sk_theme .url {
    color: #61afef;
}
.sk_theme .annotation {
    color: #56b6c2;
}
.sk_theme .omnibar_highlight {
    color: #528bff;
}
.sk_theme .omnibar_timestamp {
    color: #e5c07b;
}
.sk_theme .omnibar_visitcount {
    color: #98c379;
}
.sk_theme #sk_omnibarSearchResult ul li:nth-child(odd) {
    background: #303030;
}
.sk_theme #sk_omnibarSearchResult ul li.focused {
    background: #3e4452;
}
#sk_status, #sk_find {
    font-size: 20pt;
}`;
