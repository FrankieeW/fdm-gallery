var msBatchParser = (function()
{
    function MsBatchParser()
    {
    }

    MsBatchParser.prototype = {

        parse: function (obj)
        {
            return msParser.parse(obj);
        },

        isSupportedSource: msParser.isSupportedSource,

        supportedSourceCheckPriority: function()
        {
            return msParser.supportedSourceCheckPriority() + 1;
        },

        isPossiblySupportedSource: msParser.isPossiblySupportedSource,

        overrideUrlPolicy: msParser.overrideUrlPolicy,

        minIntevalBetweenQueryInfoDownloads: msParser.minIntevalBetweenQueryInfoDownloads
    };

    return new MsBatchParser();
}());