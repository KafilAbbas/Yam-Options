import {useState, useEffect} from "react";
// import './App.css';
// import ReactDOM from 'react-dom';   
// import axios from "axios";
import NameList from './make_table'
import Navbar from "./navbar";
import './table.css'
  const expiry_url = `ws://43.204.30.234:8000/ws/stock_updates/expiry`;


function OptionChain() {
  const [data, setdata] = useState([]);
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
    const socketUrl = `ws://43.204.30.234:8000/ws/stock_updates/${inputValue}`;

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
      <div className="Select">
      <select className= 'optionselect1' id = 'optionselect' value={select1} onChange={handleselect1}>
        <option value="">Select an option</option>
        {options.map((option, index) => (
          <option key={index} value={option}> 
            {option}
          </option>
        ))}
      </select>
      <select className = 'optionselect2'id="expiryselect" value={select2} onChange={handleselect2}>
        <option value="">Select an expiry</option>
        <option key = '0' value = '1'> {expiry_select[0]}</option>
        <option key = '1' value = '2'> {expiry_select[1]}</option>
      </select>
      </div>
    <NameList mydata={data} table_heading={tableheading} />
  </div>
);
}
export default OptionChain;
