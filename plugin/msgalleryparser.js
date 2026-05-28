var msParser = (function()
{
    function MsParser()
    {
    }

    MsParser.prototype = {

        parse: function (obj)
        {
            console.log("Parsing gallery...");
            return Promise.reject({error: "Not implemented", isParseError: true});
        },

        isSupportedSource: function(url)
        {
            return true;
        },

        supportedSourceCheckPriority: function()
        {
            return 0;
        },

        isPossiblySupportedSource: function(obj)
        {
            if (obj.contentType && !/^text\/html(;.*)?$/.test(obj.contentType))
                return false;
            return /^https?:\/\//.test(obj.url);
        },

        overrideUrlPolicy: function(url)
        {
            return true;
        },

        minIntevalBetweenQueryInfoDownloads: function()
        {
            return 300;
        }
    };

    return new MsParser();
}());