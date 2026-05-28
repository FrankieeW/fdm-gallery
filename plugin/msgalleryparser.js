var msParser = (function()
{
    function MsParser()
    {
    }

    msParser.prototype = {

        parse: function (obj)
        {
            console.log("Parsing gallery for URL:", obj.url);

            let args = ["--dump-json", "--no-check-certificate", obj.url];
            let allowWbCookies = true;
            let systemUserAgent;
            let systemBrowser;

            try {
                systemUserAgent = qtJsSystem.defaultUserAgent;
                systemBrowser = qtJsSystem.defaultWebBrowser;
                allowWbCookies = App.pluginsAllowWbCookies;
            } catch(e) {}

            // Handle proxy
            let proxyUrl = qtJsNetworkProxyMgr.proxyForUrl(obj.url).url();
            if (proxyUrl) {
                proxyUrl = proxyUrl.replace(/^https:\/\//i, 'http://');
                args.push("--proxy", proxyUrl);
            }

            // Handle cookies
            let tmpCookies;
            if (allowWbCookies && obj.cookies && obj.cookies.length) {
                tmpCookies = qtJsTools.createTmpFile("request_" + obj.requestId + "_cookies");
                if (tmpCookies && tmpCookies.writeText(cookiesToNetscapeText(obj.cookies))) {
                    args.push("--cookies", tmpCookies.path);
                }
            }

            // Handle user agent
            let userAgent = obj.userAgent || systemUserAgent;
            if (userAgent) {
                args.push("--user-agent", userAgent);
            }

            return launchPythonScript(obj.requestId, obj.interactive, "gallery_dl/__main__.py", args)
            .then(function(resultObj) {
                logPythonResult(resultObj);

                return new Promise(function(resolve, reject) {
                    let output = resultObj.output.trim();
                    if (!output) {
                        reject({error: "No output from gallery-dl", isParseError: true});
                        return;
                    }

                    // gallery-dl outputs one JSON object per line
                    let lines = output.split('\n').filter(line => line.trim());
                    if (lines.length === 0) {
                        reject({error: "No parseable output", isParseError: true});
                        return;
                    }

                    try {
                        let data = JSON.parse(lines[0]);
                        if (lines.length > 1) {
                            // Multiple items - return playlist
                            let entries = lines.map((line) => {
                                let item = JSON.parse(line);
                                return {
                                    _type: "url",
                                    url: item.url,
                                    title: item.title || item.filename
                                };
                            });
                            resolve({
                                _type: "playlist",
                                title: data.gallery_title || data.author?.name || "Gallery",
                                webpage_url: obj.url,
                                entries: entries
                            });
                        } else {
                            // Single item
                            resolve({
                                id: data.gallery_id || data.id,
                                title: data.gallery_title || data.title || "Image",
                                webpage_url: data.gallery_url || obj.url,
                                upload_date: data.date ? data.date.substring(0, 10) : null,
                                formats: [{
                                    url: data.url,
                                    ext: data.extension,
                                    protocol: "https"
                                }]
                            });
                        }
                    } catch (e) {
                        reject({error: "Failed to parse gallery-dl output: " + e.message, isParseError: true});
                    }
                });
            });
        },

        isSupportedSource: function(url)
        {
            // Let gallery-dl handle URL validation
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
            if (obj.resourceSize !== -1 &&
                    (obj.resourceSize === 0 || obj.resourceSize > 3*1024*1024))
            {
                return false;
            }
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