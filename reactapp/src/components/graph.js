
import React, { useRef, useEffect,useState } from 'react';
import Chart, { plugins } from 'chart.js/auto';

function RealTimePlot() {
  const canvasRef = useRef(null);
  const chartRef = useRef(null);
  let data_length = 0;
  useEffect(() => {
    const labels = [
    ];
    let histo = [];
    let histolable = [];
    const data = {
      labels: histolable,
      datasets: [{
        label: 'Test',
        backgroundColor: 'rgb(54, 162, 235)',
        borderColor: 'rgb(54, 162, 235)',
        data: histo,
      }]
    };
    let ismoving = false;
    let circlePosition = undefined;
    let min = 0;
    const zoomRangeSlider = {
      id:'zoomRangeSlider',
      afterDatasetsDraw(chart,args,plugins){
        const{ctx,chartArea:{left,top,right,width,bottom}} = chart;
        const angle = Math.PI/180;
        const bott = bottom+50
        const bott_circ = bottom+52.5
        const end_rect = right - 40

        circlePosition = circlePosition || left;
        ctx.beginPath();
        ctx.fillStyle = 'lightgrey';
        ctx.roundRect(left,bott,right-45,7,5);
        ctx.fill();

        ctx.beginPath();
        ctx.fillStyle = 'black';
        ctx.arc(circlePosition,bottom+52.5,10,0,360*angle,false)
        ctx.fill();
      },
      afterUpdate(chart,args,plugins){
        chart.options.scales.x.min = min;
      },
      afterEvent(chart,arc,plugins){
        
        const{ctx,canvas,chartArea:{left,top,right,width,bottom}} = chart;
        const end_rect = right - 10
        canvas.addEventListener('mousedown',(e)=>{
          ismoving = true;
        })
        canvas.addEventListener('mouseup',(e)=>{
          ismoving = false;
        })
        canvas.addEventListener('mouseout',(e)=>{
          ismoving = false;
        })
        if(arc.event.type === 'mousemove' && ismoving === true){
          const  val = arc.event.x/(end_rect);
          min = val * (data.labels.length - 1);
          console.log(data_length)
          console.log(min)
          arc.changed = true
          if(arc.event.x>=left && arc.event.x <=end_rect){
            circlePosition = arc.event.x
          }
          
        }
      }
    }
    const config = {
      type: 'line',
      data: data,
      options: {
        layout:{
          padding:{
            bottom:50,
            right:10,
            left:10,
          }
        },
        scales:{
          y:{
            beginAtZero:true
          }
        }
      },
      plugins:[zoomRangeSlider]
    };

    chartRef.current = new Chart(canvasRef.current, config);
    let variable = chartRef.current.data.labels.length+1
    const interval = setInterval(() => {
      const newLabel = variable;
      console.log(data_length)
      const newData = (variable+variable/2)%5;
      addData(chartRef.current, newLabel, newData,histolable,histo);
    }, 500);
    const chart_update = setInterval(() => {
      chartRef.current.update()
    }, 50);
    const interval2 = setInterval(()=>{
        histolable = chartRef.current.data.labels
        histo = chartRef.current.data.datasets[0]['data']
        variable++
    },1000)
    return () => {
      clearInterval(interval);
      chartRef.current.destroy();
    };
  }, []);

  function addData(chart, label, data,histolable,histo) {
    chart.data.labels = [...histolable,label]
    // console.log(int(chart.data.labels.length))
    data_length = (chart.data.labels.length)
    chart.data.datasets.forEach((dataset) => {
      dataset.data = [...histo, data];
    });
    chart.update();
  }


  
  return (
    <div>
      <canvas ref={canvasRef} id="goodCanvas1" height= {40} width={300}></canvas>
  </div>
);
}


export default RealTimePlot

