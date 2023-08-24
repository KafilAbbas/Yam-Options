// import React, { useState, useEffect } from 'react';
// import ApexCharts from 'react-apexcharts';

// function Apex() {
//   const [data, setData] = useState({
//     series: [{
//       name: 'sales',
//       data: [30, 40, 45, 50, 49, 60, 70, 91, 125]
//     }],
//     options: {
//       chart: {
//         type: 'bar'
//       },
//       xaxis: {
//         categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
//       },
//       plotOptions: {
//         bar: {
//           horizontal: false,
//           columnWidth: '55%', // Adjust the column width here
//           borderRadius: 5,
//         }
//       },
//       dataLabels: {
//         enabled: false
//       },
//       stroke: {
//         show: true,
//         width: 3 // Adjust the stroke width here
//       },
//     }
//   });

//   useEffect(() => {
//     const interval = setInterval(() => {
//       // Update the data with new values and size
//       const newData = {
//         series: [{
//           name: 'sales',
//           data: [...data.series[0].data, Math.floor(Math.random() * 100)]
//         }],
//         options: {
//           ...data.options,
//           xaxis: {
//             categories: [...data.options.xaxis.categories, data.options.xaxis.categories[data.options.xaxis.categories.length - 1] + 1]
//           }
//         }
//       };
//       setData(newData);
//     }, 1000);

//     return () => {
//       clearInterval(interval);
//     };
//   }, [data]);

//   return (
//     <div className="app">
//       <div className="row">
//         <div className="mixed-chart">
//           <ApexCharts options={data.options} series={data.series} type="line" width="500" />
//         </div>
//       </div>
//     </div>
//   );
// }

// export default Apex;

import React, { useState, useEffect } from 'react';
import ApexCharts from 'react-apexcharts';

function Apex() {
  const [histo, setHisto] = useState([]);
  const [histolable, setHistoLable] = useState([]);
  
  const initialData = {
    series: [{
      name: 'sales',
      data: histo
    }],
    options: {
      xaxis: {
        categories: histolable
      },
    }
  };

  useEffect(() => {
    const interval = setInterval(() => {
      const newRandomValue = Math.floor(Math.random() * 100);
      setHisto(prevHisto => [...prevHisto, newRandomValue]);
    }, 1000);

    const updateInterval = setInterval(() => {
      setHistoLable(prevLabels => [...prevLabels, prevLabels.length + 1]);
    }, 2000);

    return () => {
      clearInterval(interval);
      clearInterval(updateInterval);
    };
  }, []);

  const data = {
    series: [{
      name: 'sales',
      data: histo
    }],
    options: {
      chart: {
        id: "chart1",
        height: 130,
        type: "bar",
        foreColor: "#ccc",
        brush: {
          target: "chart1",
          enabled: true
        },
      xaxis: {
        categories: histolable
      },
    }
  }
}
  return (
    <div className="app">
      <div className="row">
        <div className="mixed-chart">
          <ApexCharts options={data.options} series={data.series} type="line" width="500" />
        </div>
      </div>
    </div>
  );
}

export default Apex;

  


