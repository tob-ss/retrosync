import { Gallery } from "react-grid-gallery";

function localDashboard() {
    const image1 = {
        src: "https://c2.staticflickr.com/9/8356/28897120681_3b2c0f43e0_b.jpg",
        width: 320,
        height: 212,
        customOverlay: (
            <div className="custom-overlay__caption">
            <div>Boats (Jeshu John - designerspics.com)</div>
            </div>
        ),
    }

    return (
    <Gallery images={[image1]} />
    );
}

export default localDashboard;