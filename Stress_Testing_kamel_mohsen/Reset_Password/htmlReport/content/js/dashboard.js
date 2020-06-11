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
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.6733333333333333, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [1.0, 500, 1500, "http:\/\/localhost:3001\/account\/reset-0"], "isController": false}, {"data": [1.0, 500, 1500, "http:\/\/localhost:3001\/account\/reset-1"], "isController": false}, {"data": [0.0, 500, 1500, "Reset Password"], "isController": true}, {"data": [1.0, 500, 1500, "http:\/\/localhost:3001\/account\/reset-2"], "isController": false}, {"data": [1.0, 500, 1500, "http:\/\/localhost:3001\/account\/reset-3"], "isController": false}, {"data": [1.0, 500, 1500, "http:\/\/localhost:3001\/account\/reset-4"], "isController": false}, {"data": [0.06, 500, 1500, "http:\/\/localhost:3000\/api\/v1\/users\/5e8643edd411aa54c0357fbd"], "isController": false}, {"data": [0.0, 500, 1500, "http:\/\/localhost:3000\/api\/v1\/users\/login"], "isController": false}, {"data": [1.0, 500, 1500, "http:\/\/localhost:3001\/account\/reset"], "isController": false}]}, function(index, item){
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
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 400, 1, 0.25, 588.9575000000006, 4, 5780, 35.5, 2166.0000000000005, 2611.9, 4663.720000000002, 0.8031564046703544, 1143.352819941746, 0.4458929844288052], "isController": false}, "titles": ["Label", "#Samples", "KO", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions\/s", "Received", "Sent"], "items": [{"data": ["http:\/\/localhost:3001\/account\/reset-0", 50, 0, 0.0, 6.0200000000000005, 4, 18, 5.0, 8.899999999999999, 12.899999999999991, 18.0, 0.10261440993635855, 0.20532902925742055, 0.036977262955582325], "isController": false}, {"data": ["http:\/\/localhost:3001\/account\/reset-1", 50, 0, 0.0, 20.62, 13, 277, 14.0, 19.9, 25.04999999999996, 277.0, 0.10261841138489702, 0.34623692513165943, 0.03677827829907931], "isController": false}, {"data": ["Reset Password", 50, 1, 2.0, 4607.899999999998, 2911, 8047, 4127.0, 7439.1, 7908.699999999999, 8047.0, 0.10178054892285644, 608.5220173750847, 0.26657757051865333], "isController": true}, {"data": ["http:\/\/localhost:3001\/account\/reset-2", 50, 0, 0.0, 12.419999999999995, 5, 30, 13.0, 18.799999999999997, 20.449999999999996, 30.0, 0.10261841138489702, 3.2261665212050685, 0.03757998463802381], "isController": false}, {"data": ["http:\/\/localhost:3001\/account\/reset-3", 50, 0, 0.0, 45.86000000000001, 35, 303, 41.0, 44.9, 47.79999999999998, 303.0, 0.10261440993635855, 428.3246724099097, 0.03767872864850665], "isController": false}, {"data": ["http:\/\/localhost:3001\/account\/reset-4", 50, 0, 0.0, 18.84, 12, 32, 20.0, 24.0, 25.89999999999999, 32.0, 0.10261988568144735, 123.03072038518374, 0.03798138346998881], "isController": false}, {"data": ["http:\/\/localhost:3000\/api\/v1\/users\/5e8643edd411aa54c0357fbd", 50, 0, 0.0, 2289.34, 1352, 5780, 1916.0, 4383.4, 4737.799999999999, 5780.0, 0.10213252716725223, 29.721297488433493, 0.04438376424748754], "isController": false}, {"data": ["http:\/\/localhost:3000\/api\/v1\/users\/login", 50, 1, 2.0, 2264.540000000001, 1511, 3821, 2151.5, 3054.1, 3384.999999999999, 3821.0, 0.10215673294595501, 28.392325015732137, 0.03701186320600518], "isController": false}, {"data": ["http:\/\/localhost:3001\/account\/reset", 50, 0, 0.0, 54.019999999999996, 42, 309, 47.5, 55.9, 69.34999999999991, 309.0, 0.10260598685412096, 555.0808536779629, 0.18697536276346652], "isController": false}]}, function(index, item){
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
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 400, 1, "400\/Bad Request", 1, null, null, null, null, null, null, null, null], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": ["http:\/\/localhost:3000\/api\/v1\/users\/login", 50, 1, "400\/Bad Request", 1, null, null, null, null, null, null, null, null], "isController": false}, {"data": [], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
