import { useEffect, useState, useContext } from 'react';
import useAxios from '../utils/useAxios';

const Homepage = () => {

    let api = useAxios();
    let [notes, setNotes] = useState([]);    

    useEffect(() => {
        getNotes();
    }, []);

    let getNotes = async () => {
        let response = await api.get('/api/notes/');
        response.status === 200 ? setNotes(response.data) : setNotes([]);
    };

    return(
        <div className="Homepage">
            <p>Right now, you're visiting the homepage!</p>

            <ul>
                {notes.map((note) => (
                    <li key={note.id}>{note.body}</li>
                ))}
            </ul>
        </div>
    )
};

export default Homepage;