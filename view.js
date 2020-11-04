var express = require("express");
var mysql = require("mysql");

var app = express();
app.set("view engine", "ejs");
app.set("views", "templates");

app.get("/", (req, res, next) => {
    data = {
        view_api: true,
        method: "get",
        port: 4000,
        returns: "json dump",
    };
    res.render("view", {data: data})
});

app.post("/", (req, res, next) => {
    data = {
        view_api: true,
        method: "post",
        port: 4000,
        returns: "json dump",
    };
    res.render("view", {data: data})
});

app.listen(4000, () => {
    console.log("View server running on port 4000");
});