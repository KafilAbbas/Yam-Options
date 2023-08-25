import React, { useState ,useEffect} from 'react'
import { Pie , Line} from 'react-chartjs-2'
import { Chart, registerables } from 'chart.js'
import './component.css'
Chart.register(...registerables)



function Apex (){
  const [label,setlable] = useState(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday',])
  const [data,setdata] = useState([10, 14, 17, 16, 19, 16, 17])
  const state = {
    labels: label,
    datasets: [
      {
        label: 'Class Strength',
        backgroundColor: 'rgb(54, 162, 235)',
        borderColor: 'rgb(54, 162, 235)',
        data: data,
      },
    ],
  }


  useEffect(() => {
    const config ={



      type: 'line',
      data:state,
      options:{
        // responsive: true,
        maintainAspectRatio: false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        },
        title: {
          display: true,
          text: 'Class Strength',
          fontSize: 20,
        },
        legend: {
          display: true,
          position: 'right',
        }
      }
    }
    

    const myChart = new Chart(document.getElementById('myChart'), config);

    return () => {
      myChart.destroy();
    };
  }, []);




















  return (
    <div className='task-manager'>
      <div class="chartCard">
      <div className='chartBox'>
        <canvas id="myChart"></canvas>
        
      </div>
      </div>
    </div>
  );
}
export default Apex;
