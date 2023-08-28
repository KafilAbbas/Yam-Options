import {useState, useEffect,useRef} from "react";
import Chart, { plugins } from 'chart.js/auto';
import './component.css'
import Navbar from './navbar'
const expiry_url = `ws://43.204.30.234:8000/ws/stock_updates/expiry`;
function Stradle(){
  const [data, setdata] = useState([]);
  const [expiry_date, setexpiry] = useState([]);
  const [expiry_date2, setexpiry2] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const options = ['NIFTY','BANKNIFTY','FINNIFTY','MIDCPNIFTY','CRUDEOIL','NATURALGAS'];
  const [select1,setselect1] = useState('');
  const [select2,setselect2] = useState('');
  const [expiry_select,setexpiryselect]= useState([]);
  const [histo,setHisto] = useState([]);
  const [histolable,setHistoLable] = useState([]);
  const [check_lable,setchecklable] = useState()
  const canvasRef = useRef(null);
  const chartRef = useRef(null);
  let min = 0;
  let histo2 = [];
  let histolable2 = [];
  const [spot,setspot] = useState();
  const [strike,setstrike] = useState();
  const [premium,setpremium] = useState();
  let data2 = {
    labels: histolable,
    datasets: [{
      label: 'Test',
      backgroundColor: 'rgb(54, 162, 235)',
      borderColor: 'rgb(54, 162, 235)',
      data: histo,
    }]
  };

  const [rangeval, setRangeval] = useState(null);

 
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
    const socketUrl = `ws://43.204.30.234:8000/ws/stradle/${inputValue}`;
    if(inputValue == '')
    {
      return () => {
      };
    }
    const socket = new WebSocket(socketUrl);
      socket.onmessage = event => {
          const newdata = JSON.parse(event.data);
          console.log(newdata)
          if (newdata['token']['price'] === 'dc' ){
            console.log(newdata)
            console.log('contineous data is coming')
            update_chart_persec(newdata)
          }
          else if (newdata['token']['price'] === 'df' ){
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
  let [windowSize,update_size] = useState([window.innerWidth, window.innerHeight]); 
      

  const handleselect1 = (event) =>{
    setselect1(event.target.value);
    setselect2('')
  }



  const handleselect2 = (event) =>{
    setselect2(event.target.value);
    setInputValue(select1+event.target.value)
    document.getElementById("prices").style.visibility =''
  }
  



  function change_histo_first_time(socket_data)
  {
    let check =[]
    Object.keys(socket_data).forEach(function(key, index) {
      check.push(socket_data[key]['premium'])
    });
    histo2 = check;
    histolable2 = Object.keys(socket_data)
    setHistoLable(Object.keys(socket_data))
    setHisto(check)
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
    chartRef.current.data.lables = histo_lable
    chartRef.current.data.datasets.forEach((dataset) => {
      dataset.data = histo_data;
    });
    chartRef.current.update();
  }

 

  useEffect(() => {
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
        responsive: true,
        maintainAspectRatio: false,
        scales: { 

        },

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
        }
      },
    };
    chartRef.current = new Chart(canvasRef.current, config);
    chartRef.current.canvas.parentNode.style.height = '400px';
    chartRef.current.canvas.parentNode.style.width = '1200px'     // this is the where i defint the chart idiot chart
    const chart_update = setInterval(() => {
      update_size([window.innerWidth, window.innerHeight])
      chartRef.current.update()
    }, 1000);

    return () => {
      clearInterval(chart_update)
      chartRef.current.destroy();
    };
  }, [histo]);





  function addData(chart, label, data) {
    chart.data.labels = [...histolable2,label]
    chart.data.datasets.forEach((dataset) => {
      dataset.data = [...histo2, data];
    });
    chart.update();
  };


function check(event){
  setRangeval(event.target.value)
  min = ((event.target.value)*histo.length)/100;
  chartRef.current.options.scales.x.min = min;
  chartRef.current.update()
}

  




  return (
    <div className="Main">
      <Navbar/>
      <div className="all">
      <div className="selectdrop">
      <select className='optionselect1' id = 'optionselect' value={select1} onChange={handleselect1} >
        <option value="">Select an option</option>
        {options.map((option, index) => (
          <option key={index} value={option}> 
            {option}
          </option>
        ))}
      </select>
      <select className='optionselect2' id="expiryselect" value={select2} onChange={handleselect2}>
        <option value="">Select an expiry</option>
        <option key = '0' value = '1'> {expiry_select[0]}</option>
        <option key = '1' value = '2'> {expiry_select[1]}</option>
      </select>
      </div>
      <div className = 'prices' id ='prices' style={{visibility:'hidden'}}>
      <div ><h3>spot price:  {spot}</h3></div>
      <div><h3>ATM price:  {strike} </h3></div>
      <div><h3>ATM premium = {premium} </h3></div>
      </div>
      <div className="chartCard">
      <div className='chartBox'>
        <canvas className = 'mychart'ref={canvasRef}   ></canvas>
        <input className="rangeBox" type="range" min="0" max="100" defaultValue={0} onChange={(event) => check(event)} />
      </div>
      </div>
      </div>
  </div>  
);

}
export default Stradle;
