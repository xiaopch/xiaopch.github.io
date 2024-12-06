// 在script.js中

gsap.registerPlugin(ScrollTrigger);

let iteration = 0;
const spacing = 0.1;
const snap = gsap.utils.snap(spacing);
const cards = gsap.utils.toArray('.cards li');
const cardImages = gsap.utils.toArray('.card-image');
const seamlessLoop = buildSeamlessLoop(cards, spacing);
const scrub = gsap.to(seamlessLoop, {
    totalTime: 0,
    duration: 0.5,
    ease: "power3",
    paused: true
});
const trigger = ScrollTrigger.create({
    start: 0,
    onUpdate(self) {
        if (self.progress === 1 && self.direction > 0 && !self.wrapping) {
            wrapForward(self);
        } else if (self.progress < 1e-5 && self.direction < 0 && !self.wrapping) {
            wrapBackward(self);
        } else {
            scrub.vars.totalTime = snap((iteration + self.progress) * seamlessLoop.duration());
            scrub.invalidate().restart();
            self.wrapping = false;
        }
    },
    end: "+=3000",
    pin: ".gallery"
});

function wrapForward(trigger) {
    iteration++;
    trigger.wrapping = true;
    trigger.scroll(trigger.start + 1);
}

function wrapBackward(trigger) {
    iteration--;
    if (iteration < 0) {
        iteration = 9;
        seamlessLoop.totalTime(seamlessLoop.totalTime() + seamlessLoop.duration() * 10);
        scrub.pause();
    }
    trigger.wrapping = true;
    trigger.scroll(trigger.end - 1);
}

function scrubTo(totalTime) {
    let progress = (totalTime - seamlessLoop.duration() * iteration) / seamlessLoop.duration();
    if (progress > 1) {
        wrapForward(trigger);
    } else if (progress < 0) {
        wrapBackward(trigger);
    } else {
        trigger.scroll(trigger.start + progress * (trigger.end - trigger.start));
    }
}

document.querySelector(".next").addEventListener("click", () => scrubTo(scrub.vars.totalTime + spacing));
document.querySelector(".prev").addEventListener("click", () => scrubTo(scrub.vars.totalTime - spacing));

// Autoplay functionality
let autoplayInterval = 3000; // Time interval for autoplay in milliseconds
function startAutoplay() {
    autoplay();
}

function autoplay() {
    scrubTo(scrub.vars.totalTime + spacing);
    setTimeout(startAutoplay, autoplayInterval);
}

// Start autoplay when the page loads
window.onload = startAutoplay;

function buildSeamlessLoop(items, spacing) {
    const overlap = Math.ceil(1 / spacing);
    const startTime = items.length * spacing + 0.5;
    const loopTime = (items.length + overlap) * spacing + 1;
    const rawSequence = gsap.timeline({ paused: true });
    const seamlessLoop = gsap.timeline({
        paused: true,
        repeat: -1,
        onRepeat() {
            this._time === this._dur && (this._tTime += this._dur - 0.01);
        }
    });
    const l = items.length + overlap * 2;
    let time = 0;
    let i, index, item;

    gsap.set(items, { xPercent: 400, opacity: 0, scale: 0 });

    for (i = 0; i < l; i++) {
        index = i % items.length;
        item = items[index];
        time = i * spacing;
        rawSequence.fromTo(item, { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, zIndex: 100, duration: 0.5, yoyo: true, repeat: 1, ease: "power1.in", immediateRender: false }, time)
            .fromTo(item, { xPercent: 400 }, { xPercent: -400, duration: 1, ease: "none", immediateRender: false }, time);
        i <= items.length && seamlessLoop.add("label" + i, time);
    }

    rawSequence.time(startTime);
    seamlessLoop.to(rawSequence, {
        time: loopTime,
        duration: loopTime - startTime,
        ease: "none"
    }).fromTo(rawSequence, { time: overlap * spacing + 1 }, {
        time: startTime,
        duration: startTime - (overlap * spacing + 1),
        immediateRender: false,
        ease: "none"
    });
    return seamlessLoop;
}

// 添加滚动模糊效果
ScrollTrigger.create({
    start: "top top",
    end: "bottom bottom",
    scrub: true,
    onUpdate: self => {
        const scrollProgress = self.progress;
        const centerIndex = Math.floor(cards.length / 2);
        cardImages.forEach((img, index) => {
            const distance = Math.abs(index - centerIndex);
            const blurAmount = distance * (1 - scrollProgress) * 5; // 调整5来改变模糊强度
            img.style.filter = `blur(${blurAmount}px)`;
        });
    }
});