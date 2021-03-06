var data = document.getElementById('messages')
var x_array = new Array();
var y_array = new Array();
var z_array = new Array();
var count = 0;
var data = [
        {
            opacity: 0.6,
            type: 'scatter3d',
            mode: 'lines',
            line: {
                width: 10,
                color: "green"
            },
            x: [0],
            y: [0],
            z: [0]
        }
    ];
    var layout = {
        scene: {
            aspectmode: "manual",
            aspectratio: {
                x: 1,
                y: 0.7,
                z: 1,
            },
            xaxis: {
                title: {
                    text: 'x (m)'
                },
                nticks: 9,
                range: [-1, 1],
            },
            yaxis: {
                title: {
                    text: 'y (m)'
                },
                nticks: 7,
                range: [-1, 1],
            },
            zaxis: {
                title: {
                    text: 'z (m)'
                },
                nticks: 10,
                range: [-1, 1],
            }
        },
        autosize: true,
        width: 1000,
        height: 1000,
        datarevision: count,
        margin: {
            l: 0,
            r: 0,
            b: 50,
            t: 50,
            pad: 4
        },
    };
Plotly.newPlot(document.getElementById('position'), data, layout, {showSendToCloud: false});
var socket = io.connect('http://192.168.0.164:1142')
socket.on('data', function (msg) {

    count += 1;

    x_array.push(parseFloat(msg["x"]));
    y_array.push(parseFloat(msg["y"]));
    z_array.push(parseFloat(msg["z"]));


    var data = [
        {
            opacity: 0.6,
            type: 'scatter3d',
            mode: 'lines',
            line: {
                width: 10,
                color: "green"
            },
            x: x_array,
            y: z_array,
            z: y_array
        }
    ];

    var layout = {
        scene: {
            aspectmode: "manual",
            aspectratio: {
                x: 1,
                y: 0.7,
                z: 1,
            },
            xaxis: {
                title: {
                    text: 'x (m)'
                },
                nticks: 9,
                range: [-1, 1],
            },
            yaxis: {
                title: {
                    text: 'y (m)'
                },
                nticks: 7,
                range: [-1, 1],
            },
            zaxis: {
                title: {
                    text: 'z (m)'
                },
                nticks: 10,
                range: [-1, 1],
            }
        },
        autosize: true,
        width: 1000,
        height: 1000,
        datarevision: count,
        margin: {
            l: 0,
            r: 0,
            b: 50,
            t: 50,
            pad: 4
        },
    };
    Plotly.react(document.getElementById('position'), data, layout, {showSendToCloud: false});
    console.log(msg["x"]);
    return msg
});


