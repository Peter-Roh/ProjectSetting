import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import Index from './Components/Index';
import Test from './Components/Test';

function App() {
    return (
        <BrowserRouter>
            <Route exact path="/" component={Index} />
            <Route exact path="/test" component={Test} />
        </BrowserRouter>
    );
}

export default App;
