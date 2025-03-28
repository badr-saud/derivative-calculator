window.MathJax = {
  tex: {
    inlineMath: [
      ["$", "$"],
      ["\\(", "\\)"],
    ],
    tags: "ams", // Use AMS tagging for equations
  },
  options: {
    renderActions: {
      addMenu: [0, "", ""], // Disable context menu for simplicity
    },
  },
  svg: {
    fontCache: "global", // Use global font cache for performance
  },
  loader: {
    load: ["[tex]/ams"], // Load AMS extensions for better LaTeX support
  },
};

document.addEventListener("DOMContentLoaded", function () {
  // Get the JSON data from the script tag
  const chartData = JSON.parse(
    document.getElementById("chart-data").textContent,
  );

  let xValues = chartData.xValues;
  let fValues = chartData.fValues;
  let fdValues = chartData.fdValues;
  let equation = chartData.equation;
  let der = chartData.der;

  var myDiv = document.getElementById("myDiv");
  var trace = {
    x: xValues,
    y: fValues,
    name: `fucntion`
  };

  var trace2 = {
    x: xValues,
    y: fdValues,
    name: `Derivative`
  };

  var data = [trace, trace2];

  var layout = {
    title: {
      text: "Graph",
    },
    xaxis: {
      title: {
        text: "x",
      },
    },
  };
  Plotly.newPlot(myDiv, data, layout);
  console.log(Plotly.BUILD);
});
