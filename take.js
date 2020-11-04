var express = require("express");
var mysql = require("mysql");

var app = express();
app.set("view engine", "ejs");
app.set("views", "templates");

app.get("/:lecture/:class_name", (req, res, next) => {
    lecture = req.params.lecture;
    class_name = req.params.class_name;
    data = {
        take_api: true,
        lecture: lecture,
        class_name: class_name,
        method: "get",
        port: 3000,
        returns: "json dump",
    };
    res.render("take", {data: data});
});

app.post("/:lecture/:class_name", (req, res, next) => {
    lecture = req.params.lecture;
    class_name = req.params.class_name;
    data = {
        take_api: true,
        lecture: lecture,
        class_name: class_name,
        method: "post",
        port: 3000,
        returns: "json dump",
    };
    res.render("take", {data: data});
});

app.listen(3000, () => {
    console.log("Take server running on port 3000");
});