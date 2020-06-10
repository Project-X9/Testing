/*
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/
var showControllersOnly = false;
var seriesFilter = "";
var filtersOnlySampleSeries = true;

/*
 * Add header in statistics table to group metrics by category
 * format
 *
 */
function summaryTableHeader(header) {
    var newRow = header.insertRow(-1);
    newRow.className = "tablesorter-no-sort";
    var cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Requests";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 3;
    cell.innerHTML = "Executions";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 7;
    cell.innerHTML = "Response Times (ms)";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Throughput";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 2;
    cell.innerHTML = "Network (KB/sec)";
    newRow.appendChild(cell);
}

/*
 * Populates the table identified by id parameter with the specified data and
 * format
 *
 */
function createTable(table, info, formatter, defaultSorts, seriesIndex, headerCreator) {
    var tableRef = table[0];

    // Create header and populate it with data.titles array
    var header = tableRef.createTHead();

    // Call callback is available
    if(headerCreator) {
        headerCreator(header);
    }

    var newRow = header.insertRow(-1);
    for (var index = 0; index < info.titles.length; index++) {
        var cell = document.createElement('th');
        cell.innerHTML = info.titles[index];
        newRow.appendChild(cell);
    }

    var tBody;

    // Create overall body if defined
    if(info.overall){
        tBody = document.createElement('tbody');
        tBody.className = "tablesorter-no-sort";
        tableRef.appendChild(tBody);
        var newRow = tBody.insertRow(-1);
        var data = info.overall.data;
        for(var index=0;index < data.length; index++){
            var cell = newRow.insertCell(-1);
            cell.innerHTML = formatter ? formatter(index, data[index]): data[index];
        }
    }

    // Create regular body
    tBody = document.createElement('tbody');
    tableRef.appendChild(tBody);

    var regexp;
    if(seriesFilter) {
        regexp = new RegExp(seriesFilter, 'i');
    }
    // Populate body with data.items array
    for(var index=0; index < info.items.length; index++){
        var item = info.items[index];
        if((!regexp || filtersOnlySampleSeries && !info.supportsControllersDiscrimination || regexp.test(item.data[seriesIndex]))
                &&
                (!showControllersOnly || !info.supportsControllersDiscrimination || item.isController)){
            if(item.data.length > 0) {
                var newRow = tBody.insertRow(-1);
                for(var col=0; col < item.data.length; col++){
                    var cell = newRow.insertCell(-1);
                    cell.innerHTML = formatter ? formatter(col, item.data[col]) : item.data[col];
                }
            }
        }
    }

    // Add support of columns sort
    table.tablesorter({sortList : defaultSorts});
}

$(document).ready(function() {

    // Customize table sorter default options
    $.extend( $.tablesorter.defaults, {
        theme: 'blue',
        cssInfoBlock: "tablesorter-no-sort",
        widthFixed: true,
        widgets: ['zebra']
    });

    var data = {"OkPercent": 99.75, "KoPercent": 0.25};
    var dataset = [
        {
            "label" : "KO",
            "data" : data.KoPercent,
            "color" : "#FF6347"
        },
        {
            "label" : "OK",
            "data" : data.OkPercent,
            "color" : "#9ACD32"
        }];
    $.plot($("#flot-requests-summary"), dataset, {
        series : {
            pie : {
                show : true,
                radius : 1,
                label : {
                    show : true,
                    radius : 3 / 4,
                    formatter : function(label, series) {
                        return '<div style="font-size:8pt;text-align:center;padding:2px;color:white;">'
                            + label
                            + '<br/>'
                            + Math.round10(series.percent, -2)
                            + '%</div>';
                    },
                    background : {
                        opacity : 0.5,
                        color : '#000'
                    }
                }
            }
        },
        legend : {
            show : true
        }
    });

    // Creates APDEX table
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.7144444444444444, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [0.36, 500, 1500, "http:\/\/localhost:3000\/api\/v1\/users\/5e8643edd411aa54c0357fbd"], "isController": false}, {"data": [1.0, 500, 1500, "http:\/\/localhost:3001\/home-0"], "isController": false}, {"data": [1.0, 500, 1500, "http:\/\/localhost:3001\/home-1"], "isController": false}, {"data": [0.07, 500, 1500, "http:\/\/localhost:3000\/api\/v1\/users\/login"], "isController": false}, {"data": [1.0, 500, 1500, "http:\/\/localhost:3001\/home"], "isController": false}, {"data": [1.0, 500, 1500, "http:\/\/localhost:3001\/home-2"], "isController": false}, {"data": [1.0, 500, 1500, "http:\/\/localhost:3001\/home-3"], "isController": false}, {"data": [0.0, 500, 1500, "Home"], "isController": true}, {"data": [1.0, 500, 1500, "http:\/\/localhost:3001\/home-4"], "isController": false}]}, function(index, item){
        switch(index){
            case 0:
                item = item.toFixed(3);
                break;
            case 1:
            case 2:
                item = formatDuration(item);
                break;
        }
        return item;
    }, [[0, 0]], 3);

    // Create statistics table
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 400, 1, 0.25, 454.8924999999999, 3, 5144, 31.0, 1699.7, 2080.1, 2613.8500000000004, 2.2512381809995494, 3194.1352882024566, 1.244886347647456], "isController": false}, "titles": ["Label", "#Samples", "KO", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions\/s", "Received", "Sent"], "items": [{"data": ["http:\/\/localhost:3000\/api\/v1\/users\/5e8643edd411aa54c0357fbd", 50, 0, 0.0, 1560.6399999999999, 1331, 2992, 1409.5, 2272.7999999999997, 2717.499999999999, 2992.0, 0.28457112286073655, 77.3940357183002, 0.12366616179006619], "isController": false}, {"data": ["http:\/\/localhost:3001\/home-0", 50, 0, 0.0, 3.92, 3, 5, 4.0, 4.899999999999999, 5.0, 5.0, 0.2868666701090667, 0.5740134834506618, 0.10085156371021876], "isController": false}, {"data": ["http:\/\/localhost:3001\/home-1", 50, 0, 0.0, 14.72, 13, 19, 14.0, 16.0, 17.449999999999996, 19.0, 0.28690782225486594, 0.9680337166900019, 0.10282731520267169], "isController": false}, {"data": ["http:\/\/localhost:3000\/api\/v1\/users\/login", 50, 1, 2.0, 1944.0399999999997, 1463, 5144, 1984.5, 2160.3, 2231.9, 5144.0, 0.28363483716523996, 73.47664603932314, 0.10276223104326566], "isController": false}, {"data": ["http:\/\/localhost:3001\/home", 50, 0, 0.0, 47.080000000000005, 41, 84, 46.0, 49.9, 52.89999999999999, 84.0, 0.28680085122492643, 1551.543591309504, 0.5201066218014535], "isController": false}, {"data": ["http:\/\/localhost:3001\/home-2", 50, 0, 0.0, 9.66, 4, 18, 7.5, 15.899999999999999, 16.89999999999999, 18.0, 0.2869193469715663, 9.020307165093392, 0.10507300304134509], "isController": false}, {"data": ["http:\/\/localhost:3001\/home-3", 50, 0, 0.0, 40.98000000000001, 36, 49, 40.5, 44.0, 46.449999999999996, 49.0, 0.2868683159682379, 1197.4222483770425, 0.10533445976958737], "isController": false}, {"data": ["Home", 50, 1, 2.0, 3551.760000000001, 2843, 8185, 3464.5, 4119.7, 4614.4, 8185.0, 0.2812892046829027, 1671.0969881222118, 0.7342637149583974], "isController": true}, {"data": ["http:\/\/localhost:3001\/home-4", 50, 0, 0.0, 18.1, 13, 26, 16.5, 23.9, 24.449999999999996, 26.0, 0.2869111149365926, 343.97700721222816, 0.1061907349228209], "isController": false}]}, function(index, item){
        switch(index){
            // Errors pct
            case 3:
                item = item.toFixed(2) + '%';
                break;
            // Mean
            case 4:
            // Mean
            case 7:
            // Median
            case 8:
            // Percentile 1
            case 9:
            // Percentile 2
            case 10:
            // Percentile 3
            case 11:
            // Throughput
            case 12:
            // Kbytes/s
            case 13:
            // Sent Kbytes/s
                item = item.toFixed(2);
                break;
        }
        return item;
    }, [[0, 0]], 0, summaryTableHeader);

    // Create error table
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": [{"data": ["400\/Bad Request", 1, 100.0, 0.25], "isController": false}]}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 400, 1, "400\/Bad Request", 1, null, null, null, null, null, null, null, null], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": ["http:\/\/localhost:3000\/api\/v1\/users\/login", 50, 1, "400\/Bad Request", 1, null, null, null, null, null, null, null, null], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
