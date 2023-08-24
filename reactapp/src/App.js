// import {useState, useEffect} from "react";
import './App.css';
// import ReactDOM from 'react-dom';   
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { Routes } from 'react-router-dom';


// import axios from "axios";
import OptionChain  from "./components/option_chain";
import Stradle  from './components/stradle';
import RealTimePlot from './components/graph';
import Apex from './components/apex'
// import Stradle from './components/stradle';
// const expiry_url = `ws://192.168.0.109:8000/ws/stock_updates/expiry`;


function App() {
  return (
      <Router>
          <Routes>
              <Route path="/" element={<OptionChain/>} />
              <Route path="/stradle" element={<Stradle/>} />
              <Route path="/timepass" element={<RealTimePlot/>} />
              <Route path="/apex" element={<Apex/>} />
              {/* <Route path="/contact" component={ContactPage} /> */}
          </Routes>
      </Router>
  );
}
export default App;

