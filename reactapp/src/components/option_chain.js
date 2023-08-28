import {useState, useEffect} from "react";
// import './App.css';
// import ReactDOM from 'react-dom';   
// import axios from "axios";
import NameList from './make_table'
import Navbar from "./navbar";
import './table.css'
  const expiry_url = `ws://192.168.124.38:8000/ws/stock_updates/expiry`;


function OptionChain() {
  const [data, setdata] = useState([
    [
        "OI",
        "COI",
        "volume",
        "Percentage change",
        "LTP",
        null,
        "LTP",
        "Percentage change",
        "volume",
        "COI",
        "OI"
    ],
    [
        "77385.0",
        "-70650.0",
        "198840.0",
        "5.77",
        "994.5",
        43500,
        "0.05",
        "-99.4",
        "58822260.0",
        "-1449480.0",
        "2335710.0"
    ],
    [
        "149085.0",
        "-172560.0",
        "347610.0",
        "5.77",
        "893.8",
        43600,
        "0.05",
        "-99.45",
        "28022745.0",
        "-1015605.0",
        "928125.0"
    ],
    [
        "114090.0",
        "-99120.0",
        "307575.0",
        "6.13",
        "796.7",
        43700,
        "0.1",
        "-99.07",
        "33900750.0",
        "-1123275.0",
        "1259220.0"
    ],
    [
        "131895.0",
        "-164910.0",
        "580815.0",
        "7.44",
        "694.9",
        43800,
        "0.05",
        "-99.62",
        "45606360.0",
        "-1733265.0",
        "1304160.0"
    ],
    [
        "128340.0",
        "-468735.0",
        "1541565.0",
        "7.81",
        "596.0",
        43900,
        "0.1",
        "-99.41",
        "49259745.0",
        "-2372310.0",
        "1223625.0"
    ],
    [
        "609930.0",
        "-770250.0",
        "6269265.0",
        "7.47",
        "495.5",
        44000,
        "0.1",
        "-99.56",
        "111583275.0",
        "-1940115.0",
        "3757065.0"
    ],
    [
        "278070.0",
        "-328545.0",
        "3718470.0",
        "5.6",
        "392.55",
        44100,
        "0.05",
        "-99.85",
        "85892880.0",
        "-1915320.0",
        "1315995.0"
    ],
    [
        "634320.0",
        "-420900.0",
        "13238325.0",
        "2.3",
        "296.1",
        44200,
        "0.05",
        "-99.89",
        "120407475.0",
        "-1506945.0",
        "2078745.0"
    ],
    [
        "902670.0",
        "-484635.0",
        "33316275.0",
        "-7.6",
        "195.7",
        44300,
        "0.05",
        "-99.93",
        "233342295.0",
        "-833970.0",
        "2520330.0"
    ],
    [
        "2093205.0",
        "108375.0",
        "128055885.0",
        "-34.68",
        "95.7",
        44400,
        "0.05",
        "-99.95",
        "570468990.0",
        "2179590.0",
        "5176800.0"
    ],
    [
        "9647070.0",
        "5130810.0",
        "618643050.0",
        "-99.95",
        "0.05",
        44500,
        "3.95",
        "-97.46",
        "945250125.0",
        "6212760.0",
        "8471085.0"
    ],
    [
        "4832085.0",
        "1813605.0",
        "511839570.0",
        "-99.83",
        "0.1",
        44600,
        "103.85",
        "-52.63",
        "490458930.0",
        "1553700.0",
        "2089425.0"
    ],
    [
        "3371295.0",
        "990975.0",
        "488694870.0",
        "-99.86",
        "0.05",
        44700,
        "203.95",
        "-31.26",
        "318872745.0",
        "1230150.0",
        "1451700.0"
    ],
    [
        "2839590.0",
        "408090.0",
        "430910565.0",
        "-99.54",
        "0.1",
        44800,
        "302.55",
        "-20.55",
        "201458685.0",
        "502185.0",
        "629190.0"
    ],
    [
        "2340180.0",
        "676500.0",
        "332333055.0",
        "-99.62",
        "0.05",
        44900,
        "403.0",
        "-14.75",
        "93781605.0",
        "211365.0",
        "282375.0"
    ],
    [
        "4099005.0",
        "300345.0",
        "363951375.0",
        "-98.86",
        "0.1",
        45000,
        "503.05",
        "-11.78",
        "55878465.0",
        "330390.0",
        "537195.0"
    ],
    [
        "2168700.0",
        "788835.0",
        "186999645.0",
        "-98.29",
        "0.1",
        45100,
        "603.05",
        "-9.77",
        "13433220.0",
        "218880.0",
        "233130.0"
    ],
    [
        "1343565.0",
        "235995.0",
        "166269930.0",
        "-97.62",
        "0.1",
        45200,
        "701.0",
        "-8.03",
        "6545175.0",
        "135390.0",
        "148050.0"
    ],
    [
        "1300005.0",
        "-34665.0",
        "149785395.0",
        "-98.48",
        "0.05",
        45300,
        "800.0",
        "-6.69",
        "1800150.0",
        "43785.0",
        "48735.0"
    ],
    [
        "1045545.0",
        "365745.0",
        "83315610.0",
        "-98.21",
        "0.05",
        45400,
        "902.0",
        "-7.05",
        "578550.0",
        "12060.0",
        "16515.0"
    ],
    [
        "3549180.0",
        "748425.0",
        "101924955.0",
        "-96.08",
        "0.1",
        45500,
        "1001.05",
        "-5.8",
        "622575.0",
        "-8160.0",
        "29205.0"
    ]
]);
  const [expiry_date, setexpiry] = useState([]);
  const [expiry_date2, setexpiry2] = useState([]);
  // const [inputValue1, setInputValue1] = useState('');
  const [inputValue, setInputValue] = useState('');
  const tableheading = ['CALL', 'Strike', 'PUTS'];
  const options = ['NIFTY','BANKNIFTY','FINNIFTY','MIDCPNIFTY','CRUDEOIL','NATURALGAS']
  const [select1,setselect1] = useState('')
  const [select2,setselect2] = useState('')
  const [expiry_select,setexpiryselect]= useState([])


  useEffect(()=>{
    const expiry_socket = new WebSocket(expiry_url);
    expiry_socket.onmessage = expiry =>{
      const exiprydata = JSON.parse(expiry.data);
      console.log(exiprydata.data);
      setexpiry(exiprydata.data[0]);
      setexpiry2(exiprydata.data[1]);
      console.log(expiry_date2)
      console.log(expiry_date)
    }
    return()=>{
      expiry_socket.close();
    };
// eslint-disable-next-line
  },[]);

  
  useEffect(() => {
    const socketUrl = `ws://192.168.124.38:8000/ws/stock_updates/${inputValue}`;

    const socket = new WebSocket(socketUrl);
      socket.onmessage = event => {
          const newdata = JSON.parse(event.data);
          console.log(newdata.data)
          setdata(newdata.data);
      };
      return () => {
        socket.close(1000);
        socket.onmessage = null;
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
    console.log(event.target.value)
    setselect1(event.target.value);
    // setInputValue1('1')
    setselect2('')
  }

  const handleselect2 = (event) =>{
    setselect2(event.target.value);
    setInputValue(select1+event.target.value)
  }
  
  return (
    <div className="Main">
      
      <div className="nav_bar_control">
      <Navbar/>
      </div>
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
    <NameList mydata={data} table_heading={tableheading} />
  </div>
);
}
export default OptionChain;