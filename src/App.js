import React, { useRef, useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import mapboxgl from 'mapbox-gl';
import {SmoothieChart, TimeSeries} from "smoothie"; // eslint-disable-line import/no-webpack-loader-syntax

mapboxgl.accessToken = 'pk.eyJ1IjoiYWhvYmJ5OTgiLCJhIjoiY2t1OHRoaGtpMDBieDJvcWp0OGZoN2pzbyJ9.7o5aIZFLVU4mnhXKFYMV3g';

export default function App() {
    const mapContainer = useRef(null);
    const map = useRef(null);
    const [lng, setLng] = useState(-84.3880);
    const [lat, setLat] = useState(33.7490);
    const [zoom, setZoom] = useState(9);

    useEffect(() => {
        if (map.current) return; // initialize map only once
            map.current = new mapboxgl.Map({
            container: mapContainer.current,
            style: 'mapbox://styles/ahobby98/ckv4wmk3u63hr14qm0n4dlsqa',
            center: [lng, lat],
            zoom: zoom
        });
    });

    useEffect(() => {
        if (!map.current) return; // wait for map to initialize
            map.current.on('move', () => {
            setLng(map.current.getCenter().lng.toFixed(4));
            setLat(map.current.getCenter().lat.toFixed(4));
            setZoom(map.current.getZoom().toFixed(2));
    });
});


    var smoothie = new SmoothieChart();
    smoothie.streamTo(document.getElementById("mycanvas"));
    // Data
    var line1 = new TimeSeries();
    var line2 = new TimeSeries();

// Add a random value to each line every second
    setInterval(function() {
        line1.append(new Date().getTime(), Math.random());
        line2.append(new Date().getTime(), Math.random());
    }, 1000);

// Add to SmoothieChart
    smoothie.addTimeSeries(line1);
    smoothie.addTimeSeries(line2);

    smoothie.streamTo(document.getElementById("mycanvas"), 1000 /*delay*/);



return (
    <div>
        <div className="sidebar">
            Longitude: {lng} | Latitude: {lat} | Zoom: {zoom}
        </div>
        <div ref={mapContainer} className="map-container" />
    </div>

    );
}