document.addEventListener('DOMContentLoaded', function () {
  const clearBtn = document.getElementById('clearBtn');
  const copyExpr = document.getElementById('copyExpr');
  const copyTac = document.getElementById('copyTac');
  const downloadTac = document.getElementById('downloadTac');

  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      const inp = document.getElementById('expression');
      if (inp) inp.value = '';
    });
  }

  if (copyExpr) {
    copyExpr.addEventListener('click', async () => {
      const inp = document.getElementById('expression');
      if (!inp) return;
      try {
        await navigator.clipboard.writeText(inp.value);
        copyExpr.textContent = 'Copied!';
        setTimeout(() => (copyExpr.textContent = 'Copy'), 1200);
      } catch (e) {
        console.error(e);
      }
    });
  }

  if (copyTac) {
    copyTac.addEventListener('click', async () => {
      const nodes = document.querySelectorAll('.tac-list li code');
      if (!nodes || !nodes.length) return;
      const text = Array.from(nodes).map(n => n.textContent.trim()).join('\n');
      try {
        await navigator.clipboard.writeText(text);
        copyTac.textContent = 'Copied!';
        setTimeout(() => (copyTac.textContent = 'Copy TAC'), 1200);
      } catch (e) {
        console.error(e);
      }
    });
  }

  if (downloadTac) {
    downloadTac.addEventListener('click', (e) => {
      e.preventDefault();
      const nodes = document.querySelectorAll('.tac-list li code');
      if (!nodes || !nodes.length) return;
      const text = Array.from(nodes).map(n => n.textContent.trim()).join('\n');
      const blob = new Blob([text], { type: 'text/plain;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'tac.txt';
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);
    });
  }
});
