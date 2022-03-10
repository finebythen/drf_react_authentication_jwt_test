import './App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import { AuthProvider } from './context/AuthContext';
import Header from './components/Header';
import Homepage from './pages/Homepage';
import Login from './pages/Login';
import PrivateRoute from './utils/PrivateRoute';

const App = () => {
    return(
        <div className="App">
            <Router>
                <AuthProvider>
                    <Header />
                    <Switch>
                        <PrivateRoute component={Homepage} path="/" exact/>
                        <Route component={Login} path="/login" />
                    </Switch>
                </AuthProvider>
            </Router>
        </div>
    )
};

export default App;