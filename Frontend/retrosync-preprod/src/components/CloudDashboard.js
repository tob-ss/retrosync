import { RowsPhotoAlbum } from "react-photo-album";
import "react-photo-album/rows.css";

function cloudDashboard() {
    const photos = [
        { src: "../assets/SMNE01.png",  width: 176, height: 248 },
        { src: "../assets/SNCE8P.png",  width: 176, height: 248 },
        { src: "../assets/RMCE.png",  width: 176, height: 248 },
    ];

   return <RowsPhotoAlbum 
            photos={photos}
            targetRowHeight={250}
            rowConstraints={{ maxPhotos: 4, singleRowMaxHeight: 250 }} 
            />

}

export default cloudDashboard;