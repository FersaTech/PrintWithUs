import React from 'react';
import './index.css';
import App from './App';
import { createRoot } from "react-dom/client"


const container = document.getElementById('root');
if(!container) throw new Error("Failed to find the root Element");
const root = createRoot(container);
root.render(<App />);


// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
