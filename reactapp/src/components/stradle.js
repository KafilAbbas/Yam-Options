import {useState, useEffect,useRef} from "react";
import Chart, { plugins } from 'chart.js/auto';

const expiry_url = `ws://192.168.0.102:8000/ws/stock_updates/expiry`;
// const sleep = ms => new Promise(r => setTimeout(r, ms));
function Stradle(){
  const [data, setdata] = useState([]);
  const [expiry_date, setexpiry] = useState([]);
  const [expiry_date2, setexpiry2] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const tableheading = ['CALL', 'Strike', 'PUTS'];
  const options = ['NIFTY','BANKNIFTY','FINNIFTY','MIDCPNIFTY','CRUDEOIL','NATURALGAS'];
  const [select1,setselect1] = useState('');
  const [select2,setselect2] = useState('');
  const [expiry_select,setexpiryselect]= useState([]);
  const [histo,setHisto] = useState([]);
  const [histolable,setHistoLable] = useState([]);
  const [check_lable,setchecklable] = useState()
  const canvasRef = useRef(null);
  const chartRef = useRef(null);
  let ismoving = false;
  let circlePosition = undefined;
  let min = 0;
  let histo2 = [];
  let histolable2 = [];
  let check_lable2;
  const [spot,setspot] = useState();
  const [strike,setstrike] = useState();
  const [premium,setpremium] = useState();
  const data2 = {
    labels: histolable,
    datasets: [{
      label: 'Test',
      backgroundColor: 'rgb(54, 162, 235)',
      borderColor: 'rgb(54, 162, 235)',
      data: histo,
    }]
  };
  // let histo = [];
  // let histolable = [];



  useEffect(()=>{
    const expiry_socket = new WebSocket(expiry_url);
    expiry_socket.onmessage = expiry =>{
      const exiprydata = JSON.parse(expiry.data);
      setexpiry(exiprydata.data[0]);
      setexpiry2(exiprydata.data[1]);
    }
    return()=>{
      expiry_socket.close();
    };
  },[]);



  
  useEffect(() => {
    const socketUrl = `ws://192.168.0.102:8000/ws/stradle/${inputValue}`;
    if(inputValue == '')
    {
      return () => {
        // socket.close();
        // socket.onmessage = null;
      };
    }
    const socket = new WebSocket(socketUrl);
      socket.onmessage = event => {
          const newdata = JSON.parse(event.data);
          console.log(newdata)
          if (newdata['token']['price'] === 'dc' ){
            console.log(newdata)
            // delete newdata['token']
            console.log('contineous data is coming')
            update_chart_persec(newdata)
          }
          else if (newdata['token']['price'] === 'df' ){
            // console.log(newdata)
            delete newdata['token']
            change_histo_first_time(newdata)
            console.log('first data is here')
          }
          else if (newdata['token']['price'] === 'du' ){
            console.log(newdata)
            console.log('the update data is here')
            update_histo_everymin(newdata)
          }
      };
      return () => {
        socket.close();
        // socket.onmessage = null;
      };
  }, [inputValue]);

 

  useEffect(()=>{
    if (select1 === 'NIFTY'){
      setexpiryselect([expiry_date[0],expiry_date2[0]]);
    }
    else if (select1 === 'BANKNIFTY'){
      setexpiryselect([expiry_date[1],expiry_date2[1]]);
    }
    else if (select1 === 'FINNIFTY'){
      setexpiryselect([expiry_date[2],expiry_date2[2]]);
    }
    else if (select1 === 'MIDCPNIFTY'){
      setexpiryselect([expiry_date[3],expiry_date2[3]]);
    }
    else if (select1 === 'CRUDEOIL'){
      setexpiryselect([expiry_date[4],expiry_date2[4]]);
    }
    else if (select1 === 'NATURALGAS'){
      setexpiryselect([expiry_date[5],expiry_date2[5]]);
    }
  },[select1,expiry_date,expiry_date2])

  

  const handleselect1 = (event) =>{
    setselect1(event.target.value);
    setselect2('')
  }



  const handleselect2 = (event) =>{
    setselect2(event.target.value);
    setInputValue(select1+event.target.value)
  }
  



  function change_histo_first_time(socket_data)
  {
    let check =[]
    Object.keys(socket_data).forEach(function(key, index) {
      check.push(socket_data[key]['premium'])
    });
    // setTimeout()
    // console.log(check);
    // await sleep(2000);
    histo2 = check;
    histolable2 = Object.keys(socket_data)
    setHistoLable(Object.keys(socket_data))
    setHisto(check)
    // console.log(histo)
    // console.log(Object.keys(socket_data))
    // setHisto(check, () => {
    //   console.log(histo); // This should log the updated histo
    // });
    // setHistoLable(Object.keys(socket_data), () => {
    //   console.log(histolable); // This should log the updated histolable
    // });
    update_data(Object.keys(socket_data),check)
  }
  function update_histo_everymin(data)
  {
    histolable2 = [...histolable2,Object.keys(data)[0]];
    histo2 = [...histo2,data[Object.keys(data)[0]]['premium']];
    
  }

  function update_chart_persec(data){
    const newLabel = Object.keys(data)[0];
      const newData = data[newLabel]['premium'];
      addData(chartRef.current, newLabel, newData);
      // setHisto(histo)
      setspot(data[Object.keys(data)[0]]['spot']);
      setstrike(data[Object.keys(data)[0]]['price']);
      setpremium(data[Object.keys(data)[0]]['premium']);
      setchecklable(newLabel)
  }



  function update_data(histo_lable,histo_data){
    // console.log(histo)
    // console.log(histolable)
    // console.log(histo_data)
    // console.log(histo_lable)
    chartRef.current.data.lables = histo_lable
    // console.log(chartRef.current.data.lables)
    chartRef.current.data.datasets.forEach((dataset) => {
      dataset.data = histo_data;
    });
    // console.log(chartRef.current.data.datasets[0].data)
    chartRef.current.update();
    // histolable = Object.keys(socket_data);
    // histo = check;
  }

 

  useEffect(() => {
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
          min = val * data2.labels.length - 1;
          arc.changed = true
          if(arc.event.x>=left && arc.event.x <=end_rect){
            circlePosition = arc.event.x
          }
          
        }
      }
    }
    const config = {
      type: 'line',
      data: data2,
      options: {
        animation : true,
        elements:{
          line:{
            borderWidth:1.5
          },
          point:{
            pointStyle :false
          }
        },
        maintainAspectRatio:true,
        plugins: {
          legend: {
              usePointStyle:false,
              display: true,
              labels: {
                  color: 'rgb(54, 162, 235)'
              }
          }
      },
        layout:{
          padding:{
            bottom:50,
            right:10,
            left:10,
          }
        },
        scales:{
          y:{
            beginAtZero:false
          }
        }
      },
      plugins:[zoomRangeSlider]
    };
    chartRef.current = new Chart(canvasRef.current, config);
    // let variable = chartRef.current.data.labels.length+1
    // const interval = setInterval(() => {
    //   const newLabel = variable;
    //   const newData = 300;
    //   addData(chartRef.current, newLabel, newData);
    // }, 50);
      const chart_update = setInterval(() => {
        chartRef.current.update()
      }, 100);
    // const interval2 (){  
    //     histolable = chartRef.current.data.labels
    //     histo = chartRef.current.data.datasets[0]['data']
    //     variable++
    // },)
    return () => {
      // clearInterval(interval);
      clearInterval(chart_update)
      chartRef.current.destroy();
    };
  }, [histo]);







  function addData(chart, label, data) {
    console.log(histolable2)
    chart.data.labels = [...histolable2,label]
    console.log(label)
    console.log(chart.data.labels)
    console.log(data)
    chart.data.datasets.forEach((dataset) => {
      dataset.data = [...histo2, data];
    });
    console.log(chart.data.labels)
    chart.update();
  }



  




  return (
    <div>
      
      <select id = 'optionselect' value={select1} onChange={handleselect1}>
        <option value="">Select an option</option>
        {options.map((option, index) => (
          <option key={index} value={option}> 
            {option}
          </option>
        ))}
      </select>
      <select id="expiryselect" value={select2} onChange={handleselect2}>
        <option value="">Select an expiry</option>
        <option key = '0' value = '1'> {expiry_select[0]}</option>
        <option key = '1' value = '2'> {expiry_select[1]}</option>
      </select>
      <div><h3>spot price:  {spot}</h3></div>
      <div><h3>ATM price:  {strike} </h3></div>
      <div><h3>ATM premium = {premium} </h3></div>
      <canvas ref={canvasRef} id="goodCanvas1" height= {100} width={200}></canvas>
      <input type="range"></input>
  </div>
);









}
export default Stradle;