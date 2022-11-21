type Status = 'idle' | 'downloading' | 'complete';

function downloadStatus(status: Status) {
    if (status === 'idle') {
        console.log("Download");
    } else if (status === 'downloading') {
        console.log("Downloading...");
    } else if (status === 'complete') {
        console.log("Your download is complete!");
    }
}


downloadStatus('complete');
