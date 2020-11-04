var express = require("express");
var mysql = require("mysql");

var app = express();
app.set("view engine", "ejs");
app.set("views", "templates");

app.get("/", (req, res, next) => {
    data = {
        modify_api: true,
        method: "get",
        port: 5000,
        returns: "json dump",
    };
    res.render("modify", {data: data})
});

app.post("/", (req, res, next) => {
    data = {
        modify_api: true,
        method: "post",
        port: 5000,
        returns: "json dump",
    };
    res.render("modify", {data: data})
});

app.listen(5000, () => {
    console.log("Modify server running on port 5000");
});
