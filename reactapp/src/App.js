  
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { Routes } from 'react-router-dom';
import OptionChain  from "./components/option_chain";
import Stradle  from './components/stradle';
import Home from './components/home';

function App() {
  return (
    
      <Router>
          <Routes>
              <Route path="/" element={<Home/>} />
              <Route path="/stradle" element={<Stradle/>} />
              <Route path="/option_chain" element={<OptionChain/>} />
          </Routes>
      </Router>

    
  );
}
export default App;

