var http = require("http");

http
  .createServer(function(req, res){
    res.write("Hello world! It's good to be here.");
    res.end();
  })
  .listen(8000);
