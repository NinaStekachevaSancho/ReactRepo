import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import React from 'react';
import logo from './logo.svg';
import './App.css';
import Rating from "./pages/Rating";
import Recorder from "./pages/Recorder";
import Terms from "./pages/Terms";
import HomeLayout from "./layouts/HomeLayout";
import Gracias from "./pages/Gracias";
import PruebaFunc from "./pages/PruebaFunc";
import GetQuestion from "./pages/GetQuestion";

function App() {
  return (
    <div className="App">
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<HomeLayout />}> 
              <Route path="/getquestion" element={<GetQuestion />}  />
              <Route path="/rating/:question" element={<Rating />} />
              <Route path="/recorder" element={<Recorder />} />
              <Route path="/terms" element={<Terms />} />
              <Route path="/gracias" element={<Gracias />} />
              <Route path="/pruebafunc" element={<PruebaFunc />} />
            </Route>
          </Routes>
        </BrowserRouter>
    </div>
  );
}

export default App;
