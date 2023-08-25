// import {useState, useEffect} from "react";
// import './App.css';
// import ReactDOM from 'react-dom';   
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { Routes } from 'react-router-dom';


// import axios from "axios";
import OptionChain  from "./components/option_chain";
import Stradle  from './components/stradle';
import RealTimePlot from './components/graph';
import Apex from './components/apex'
import Stradle2 from './components/idontknow';
import Navbar from './components/navbar';
// import Stradle from './components/stradle';
// const expiry_url = `ws://192.168.0.109:8000/ws/stock_updates/expiry`;


function App() {
  return (
    
      <Router>
          <Routes>
              <Route path="/" element={<Navbar/>} />
              <Route path="/stradle" element={<Stradle/>} />
              <Route path="/timepass" element={<RealTimePlot/>} />
              <Route path="/apex" element={<Apex/>} />
              <Route path="/stradle2" element={<Stradle2/>} />
              <Route path="/option_chain" element={<OptionChain/>} />
          </Routes>
      </Router>

    
  );
}
export default App;

