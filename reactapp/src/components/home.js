import {useState, useEffect,useRef} from "react";
import Navbar from './navbar'
import './component.css'
function Home(){
    return(
        <div>
            <div>
            <Navbar/>
            </div>
        <div className="HomeBox">
        <div className="Home">
            <h2>Welcome To Yam Options</h2>
        </div>
        </div>
        </div>
    );
}
export default Home